# ChatGPT API Integration and Flask Web App Development
The ChatGPT Web Application is a chatbot made using Flask that uses the OpenAI GPT-3.5 Turbo API to generate responses to user input. The chatbot is designed to answer questions and provide information on a variety of topics

## Installation
1. Clone this repository to your local machine.
2. Set up a virtual environment
3. Install the required packages listed in requirements.txt 
 ```sh
    pip install -r requirements.txt
```

4. Get an API key for the [OpenAI API](https://platform.openai.com/) and replace the placeholder `API_KEY` in `app.py` with your API key.
5. Run `app.py` using your preferred method.

### Note
For testing the app run the following command:
```sh
    python -m unittest
```

## Usage
Navigate to [localhost:5000](http://127.0.0.1:5000) in your web browser. Type your message or question in the input field and press Enter or click "Send".
The chatbot will generate a response based on your input and display it on the screen.

To see the live version, visit [here](http://ribyaann.pythonanywhere.com)

## API Calls
This application uses OpenAI GPT-3.5 Turbo API to generate responses. To use the API, you must have an API key, which you can get from the OpenAI website.

An example API call looks as follows:
 ```python
 # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```
An example API response looks as follows:
```
{
 'id': 'chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve',
 'object': 'chat.completion',
 'created': 1677649420,
 'model': 'gpt-3.5-turbo',
 'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87},
 'choices': [
   {
    'message': {
      'role': 'assistant',
      'content': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'},
    'finish_reason': 'stop',
    'index': 0
   }
  ]
}
```
The assistant’s reply can be extracted with `response['choices'][0]['message']['content']`


