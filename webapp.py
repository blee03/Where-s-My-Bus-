from flask import Flask, render_template, request, redirect
from apicalls import grab_routes, grab_stops, bus_ETA 
import json
app = Flask(__name__)
#route page render
@app.route('/')
def routes():
    routelist = []
    routelist = grab_routes('1')
    return render_template('index.html', routelist=routelist)
@app.route('/move', methods=['POST'])
def movetostops():
    val = request.form['route_chosen']
    value = {'val': val, 'val2': 0} 
    with open('values.txt', 'w') as json_file:
        json.dump(value, json_file)
    print(val)
    return redirect('/stops')
@app.route('/stops')
def stops():
    stoplist = []
    with open('values.txt') as f:
        value_data = json.load(f) 
    stoplist=grab_stops(int(value_data['val']),'1')[0]
    return render_template('location.html', stoplist=stoplist)
@app.route('/return', methods=['POST'])
def movetoeta():
    val2 = request.form['stop_chosen']
    with open('values.txt') as f:
        value_data = json.load(f)
    value_data['val2'] = val2
    with open('values.txt', 'w') as json_file:
        json.dump(value_data, json_file)
    return redirect('/eta')
@app.route('/eta')
def eta():
    arrivals = []
    with open('values.txt') as f:
        value_data = json.load(f)
    arrivals=bus_ETA(int(value_data['val2']), grab_stops(int(value_data['val']), '1')[1])
    return render_template('eta.html', arrivals=arrivals)
if __name__ == '__main__':
    app.run()
