from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
PORT = 8080

title = 'Devs in the Shed'

@app.route('/')
def index():
    return render_template('index.html', title = title)

if __name__ == '__main__':
   app.run(debug = False, host="0.0.0.0", port=PORT)