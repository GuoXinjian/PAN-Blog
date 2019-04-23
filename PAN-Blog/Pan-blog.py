from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Guo3625202123@132.232.77.200:3306/Pan-blog'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SECRET_KEY"] = "12345678"

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


@app. route('/',methods=['GET','POST']) 
def index(): 

    form = NameForm() 
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data 
        return redirect(url_for('index'))
    return render_template('index.html', form=form,name=session.get('name'),current_time=datetime.utcnow())


@app. route('/user/<name>') 
def user( name): 
    return render_template('user.html', name= name)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>'% self.name

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username




# @app.route('/',methods=['GET','POST'])
# def index():
#     if request.method=='GET':
#         return render_template('index.html')
#     elif request.method=='POST':
#         print(request.args.to_dict())
#         return 'POST'
    

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         print('aaa')
#     else:
#         return render_template('test.html')
#     return 'OK'

if __name__ == '__main__':
    app.run(debug=True)