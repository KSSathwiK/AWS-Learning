from flask import *

app = Flask(__name__)

@app.route('/user/<name>')
def message(name):
    return render_template('index.html',name=name)


if __name__ == "__main__":
    app.run(debug=True)