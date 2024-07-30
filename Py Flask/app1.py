from flask import Flask

app=Flask(__name__)

@app.route('/')
def sathwik():
    return 'Hi this is Sathwik'





if __name__ == '__main__':
    app.run()