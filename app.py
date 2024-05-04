from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return 'You are in the home page now.'


if __name__ == "__main__":
    app.run(debug=True)