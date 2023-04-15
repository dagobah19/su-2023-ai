import promptSync from 'prompt-sync';
import { Configuration, OpenAIApi } from 'openai';

const config = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(config);

const input = promptSync({sigint: true});

while (true) {

    let lang = input('Enter language: ');
    let code = input('Enter your code: ');

    let prompt = `Please review the following ${lang} code and provide feedback:\n ${code}`;

    const completion = await openai.createCompletion({
        model: 'text-davinci-002',
        prompt,
        max_tokens: 200,
        n: 1,
        stop: 'None',
        temperature: 0.7,
    });
    console.log(completion.data.choices[0].text);

}