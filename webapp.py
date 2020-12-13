from flask import Flask, render_template, request, redirect
from apicalls import grab_routes, grab_stops, bus_ETA 
app = Flask(__name__)
val = 0
val2 = 0
#route page render
@app.route('/')
def routes():
    routelist = []
    routelist = grab_routes('1')
    return render_template('index.html', routelist=routelist)
@app.route('/move', methods=['POST'])
def movetostops():
    val = str(request.form['route_chosen'])
    return redirect('/stops')
@app.route('/stops')
def stops():
    stoplist = []
    stoplist=grab_stops(int(val),'1')
    return render_template('location.html', stoplist=stoplist)
@app.route('/return', methods=['POST'])
def movetoeta():
    val2 = str(request.form['stop_chosen'])
    return redirect('/eta')
@app.route('/eta')
def eta():
    arrivals = []
    arrivals=bus_ETA(int(val2))
    return render_template('eta.html', arrivals=arrivals)
if __name__ == '__main__':
    app.run()
