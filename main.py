from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

from forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


if __name__=="__main__":
    app.run(debug=True,port=8888)
