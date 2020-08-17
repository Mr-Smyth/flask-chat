import os
from flask import Flask, redirect


app = Flask(__name__)
messages = []


def add_messages(username, message):
    """ Add messages to the messages list """
    messages.append(f"{username}: {message}")


def get_all_messages():
    """ Get all the messages and separate them with the 'br' tag"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """Main page with with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """ Display a chat message """
    return f"<h1>Welcome, {username}</h1>{get_all_messages()}"


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a chat message and then redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
