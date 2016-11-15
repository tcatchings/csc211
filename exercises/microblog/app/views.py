from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Puff'}
    posts = [
        {
            'author': {'nickname': 'tristanPuff'},
            'body': 'jiggs is teh best in ze may lay'
        },
        {
            'author': {'nickname': 'skrub'},
            'body': 'nah fam, jiggs be lame! hur hur'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)
