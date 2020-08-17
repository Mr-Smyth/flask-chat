import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_message(username, message):
    """ Add messages to the messages list """
    now = datetime.now().strftime("%I:%M:%S%P")
    messages.append({"timestamp": now, "from": username, "message": message})


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
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    """ Add and display a chat message """

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template(
        "chat.html", username=username, chat_messages=messages)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
