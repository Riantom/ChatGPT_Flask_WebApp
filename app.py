from flask import Flask, render_template, request
import openai
import key
openai.api_key = key.API_KEY
app = Flask(__name__)
global messages
# To give gpt an initial context
messages = [{'role': 'system', 'content': 'Give response using the context given'}, {
    'role': 'assistant', 'content': 'What is your question or prompt?'}]


def gpt_response(message):
    prompt = {'role': 'user', 'content': message}
    messages.append(prompt)  # to get responses with context
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    if completion.choices[0].message != None:
        messages.append(dict(completion.choices[0].message))
        return completion.choices[0].message['content']
    else:
        return 'Failed to Generate response!'

# define the Flask app routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    message = request.form['message']
    response = gpt_response(message)
    return render_template('result.html', message=message, response=response)


if __name__ == '__main__':
    app.run(debug=True)
