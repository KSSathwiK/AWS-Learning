#URL Routing

from flask import *

app=Flask(__name__)

@app.route('/admin')
def admin():
    return 'This is Admin'

@app.route('/student')
def student():
    return 'This is Student'

@app.route('/staff')
def staff():
    return 'This is Staff'

@app.route('/user/<name>')
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    if name == "student":
        return redirect(url_for('student'))
    if name == "staff":
        return redirect(url_for('staff'))
    

if __name__ == "__main__":
    app.run(debug=True)





if __name__ == '__main__':
    app.run()