import flask

app = flask.Flask(__name__)
app.secret_key = b'nahodny retezec'
