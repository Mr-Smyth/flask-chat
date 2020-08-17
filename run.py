import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    """ Add messages to the messages list """
    now = datetime.now().strftime("%I:%M:%S%P")
    messages_dict = {"timestamp": now, "from": username, "message":message}
    messages.append(messages_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with with instructions"""
    # if there is a Post method
    if request.method == "POST":
        # then the form username is the sessions username
        session["username"] = request.form["username"]

    if "username" in session:
        """ so if there is a username, redirect to the user function in the
        username route below"""
        return redirect(session["username"])

    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """ Display a chat message """
    return render_template("chat.html", username = username, chat_messages = messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a chat message and then redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
