from flask import Flask, render_template
from main import callroute
app = Flask(__name__)

@app.route('/')
def grabroutenames():
    test = callroute
@app.route('/signup', methods = ['POST'])
def grabnumber():
    usernumber = request.form['routenumber']
    return redirect('/')

if __name__ == '__main__':
    app.run()
