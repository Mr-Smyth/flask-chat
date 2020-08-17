import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello there you load of old fogeys</h1>"


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)

