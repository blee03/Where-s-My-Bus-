from flask import Flask, render_template
from apicalls import grab_routes
app = Flask(__name__)
#route page render
@app.route('/')
def routes():
    routelist = []
    routelist = grab_routes('1')
    return render_template('index.html', routelist=routelist)

@app.route('/', methods=['POST'])
def user_route():
    var = request.form['routechosen']
    return var
#stop page render 
#@app.route('/stops')
#def stops():
    #return render_template('stops.html')

if __name__ == '__main__':
    app.run()
