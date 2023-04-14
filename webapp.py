from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>AP SHACO PENTAKILL IN ARAM\n</p><p>AP SHACO PENTAKILL IN ARAM\n</p>"