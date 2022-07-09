# set FLASK_APP=flaskblog.py
# set flask_debug=1
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 1, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July 3, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts);

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ =='__main__':  
    app.run(debug=True)