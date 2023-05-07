from flask import Flask, render_template, request, session
import openai
import uuid
import key
openai.api_key = key.API_KEY
app = Flask(__name__)
app.secret_key = 'ANY_SECRET_KEY'
app.config['SESSION_TYPE'] = 'filesystem'
# define the Flask app routes


def gpt_response(message, session_id):
    messages = session.get(session_id, [{'role': 'system', 'content': 'Give response using the context given'}, {
                           'role': 'assistant', 'content': 'What is your question or prompt?'}])  # Retrieve the context for the session ID
    prompt = {'role': 'user', 'content': message}
    messages.append(prompt)  # to get responses with context
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    if completion.choices[0].message != None:
        messages.append(dict(completion.choices[0].message))
        # Store the updated context for the session ID
        session[session_id] = messages
        return completion.choices[0].message['content']
    else:
        return 'Failed to Generate response!'


@app.route("/")
def index():
    if 'session_id' not in session:
        # Generate a new session ID if it doesn't exist
        session['session_id'] = str(uuid.uuid4())
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    message = request.form['message']
    if session:
        session_id = session['session_id']
    else:
        # for testing to work for the result only
        session_id = request.args.get('session_id')
    response = gpt_response(message, session_id)
    return render_template('result.html', message=message, response=response)


if __name__ == '__main__':
    app.run(debug=True)
