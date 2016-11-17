from flask import render_template
from app import app, lm
from .forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

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

#def login('/login', methods=['GET', 'POST']):
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for OpenID="%s", remember_me=%s' %
#              (form.openid.data, str(form.remember_me.data)))
#        return redirect('/index')
#    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
