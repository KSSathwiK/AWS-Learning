#GET HTTP
from flask import *

app = Flask(__name__)

@app.route('/login',methods = ['GET'])
def login():
    user_name = request.args.get('uname')
    password = request.args.get('pwd')

    if user_name == 'sathwik' and password == "google":
        return 'Welcome %s' %user_name
    else:
        return 'Invalid Password!, Retry Again!'
    



if __name__ == "__main__":
    app.run(debug=True)