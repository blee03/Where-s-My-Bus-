from flask import Flask, render_template
import apicalls
app = Flask(__name__)
#route page render
@app.route('/')
def routes():
    routelist = grab_routes("1")
    return render_template('index.html', routelist=routelist)

#stop page render 
#@app.route('/stops')
#def stops():
    #return render_template('stops.html')

if __name__ == '__main__':
    app.run()
