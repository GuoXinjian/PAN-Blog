from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail,Message

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import os
from threading import Thread

app           = Flask(__name__)

baseidr = os.path.abspath(os.path.dirname(__file__))

#app.config['DEBUG']                          = True

#app.config['SECRET_KEY']                     = 'hard to guess string'
#app.config['SQLALCHEMY_DATABASE_URI']        = "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']  = True
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['MAIL_SERVER']                    = 'smtp.126.com'
#app.config['MAIL_PROT']                      = 25
#app.config['MAIL_USE_TLS']                   = True
#app.config['MAIL_USE_SSL']                   = False
#app.config['MAIL_USERNAME']                  = os.environ.get('MAIL_USERNAME')
#app.config['MAIL_PASSWORD']                  = os.environ.get('MAIL_PASSWORD')
#app.config['FLASKY_MAIL_SUBJECT_PREFIX']     = '[Pan平底锅]'
#app.config['FLASKY_MAIL_SENDER']             = 'Pan Admin <follow_wind@126.com>'
#app.config['FLASKY_ADMIN']                   = os.environ.get('FLASKY_ADMIN')



manager       = Manager(app)
bootstrap     = Bootstrap(app)
moment        = Moment(app)
db            = SQLAlchemy(app)
migrate       = Migrate(app,db)
mail          = Mail(app)






@app.route('/',methods=['GET','POST'])
def index():
    # user_agent=request.headers.get('User-Agent')
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username= form.name.data)
            db.session.add(user)
            session['known']=False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'] ,'New User','mail/new_user',user=user)
        else:
            session['known'] =True
        session['name'] = form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',current_time=datetime.utcnow(),form=form,name=session.get('name'),known = session.get('known',False))
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



class NameForm(FlaskForm):
    name   = StringField('姓名',validators=[DataRequired()])
    submit = SubmitField('确定')

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(to,subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
                    sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # mail.send(msg)
    # print('sent')
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)



if __name__=='__main__':
    manager.run()