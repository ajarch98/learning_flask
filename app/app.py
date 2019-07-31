from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Advait'}
    return render_template("index.html", title = "Hello", user = user)