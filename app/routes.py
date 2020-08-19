from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    #return 'Hello, World!'
    user = {'username':'Miguel'}
    return render_template('index.html', title="Home", user=user) 
