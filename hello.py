from flask import Flask

app = Flask(__name__)#創造物件 links our module to the Flask object


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
