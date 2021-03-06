import flask
from delta.blueprints.content  import content
from delta.blueprints.logs     import logs
from delta.blueprints.users    import users

app = flask.Flask(__name__)

app.register_blueprint(content)
app.register_blueprint(logs)
app.register_blueprint(users)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

