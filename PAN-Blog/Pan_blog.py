from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_script import Shell,Manager
from datetime import datetime
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import os
from threading import Thread


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]        = "mysql+pymysql://root:guo3625202123@132.232.77.200:3306/Pan-blog?charset=utf8mb4"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]  = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['FLASKY_MAIL_PREFIX']             = '[平底锅]'
app.config['FLASKY_MAIL_SENDER']             = '平底锅 Admin'
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.126.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'follow_wind@126.com',
    MAIL_PASSWORD = 'XG2tX5dEtxER',
    # MAIL_PASSWORD = 'poippvcqweanbbcc' 763532119@qq.com
    MAIL_DEBUG = True
)

app.config['FLASKY_ADMIN']                   = os.environ.get('FLASKY_ADMIN')
app.config["SECRET_KEY"]                     = "12345678"

bootstrap = Bootstrap(app)
moment    = Moment(app)
db        = SQLAlchemy(app)
manager   = Manager(app)
mail      = Mail(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell',Shell(make_shell_context))

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwards):
    msg = Message(app.config['FLASKY_MAIL_PREFIX'] + subject,
                    sender='follow_wind@126.com', recipients=[to])
                #   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwards )
    msg.html = render_template(template + '.html', **kwards)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    print('send_mail')
    return thr


@app. route('/',methods=['GET','POST']) 
def index(): 

    form = NameForm() 
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known']=False
            send_email('follow_wind@126.com','New User','mail/new_user',user=user)
            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'], 'New User',
            #                 'mail/new_user', user=user)
        else:
            session['known']=True

        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed your name!')
        session['name'] = form.name.data 
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html', form=form,name=session.get('name'),known=session.get('known',False),current_time=datetime.utcnow())


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
    users = db.relationship('User', backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>'% self.name

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username



if __name__ == '__main__':
    manager.run()