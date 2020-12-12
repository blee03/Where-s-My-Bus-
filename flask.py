from flask import Flask, render_template

app = Flask(__name__)
title = "Bus Transit Time of Arrival - Vincent Song, Brian Lee, Ethan Lau"
date = "12/12/2020 - 12/13/2020"
category = "Beginner"

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template('about.html', title = title, date = date, category = category )
if __name__ == "__main__":
    app.run()