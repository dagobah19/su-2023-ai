import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    while True:
        lang = input("Enter language or type 'quit':").strip()
        if lang.lower() == 'quit':
            break
        
        code = ""
        print("Enter your code (type 'FIN' at the end of the code, or 'quit' to, you know, quit:)")

        while True:
            lines = input()
            if lines.lower() == 'fin':
                break
            if lines.lower() == 'quit':
                return
            code += lines + "\n"
        
        query = f"Please review the following {lang} code and provide feedback:\n {code}"

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=query,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7
        )
        print(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
