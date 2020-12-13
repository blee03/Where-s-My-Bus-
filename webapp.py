from flask import Flask, render_template, request, redirect
from apicalls import grab_routes, grab_stops
app = Flask(__name__)
#route page render
@app.route('/')
def routes():
    routelist = []
    routelist = grab_routes('1')
    return render_template('index.html', routelist=routelist)

@app.route('/', methods=['POST'])
def user_route():
    val = request.form['routechosen']
    return val
@app.route('/move', methods=['POST'])
def movetostops():
    return redirect('/stops')
@app.route('/stops')
def stops():
    stoplist = []
    stoplist=grab_stops(user_route())
    return render_template('location.html', stoplist=stoplist)

if __name__ == '__main__':
    app.run()
