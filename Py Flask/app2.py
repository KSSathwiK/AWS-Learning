from flask import *

app = Flask(__name__)

def sathwik():
    return "My name is Sathwik"

app.add_url_rule('/sathwik','sathwik',sathwik)


if __name__ == "__main__":
    app.run(debug=True)