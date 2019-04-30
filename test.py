from flask import Flask
from flask_script import Manager
from flask_mail import Mail,Message

app=Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'follow_wind@126.com'#'763532119@qq.com'
app.config['MAIL_PASSWORD'] = 'XG2tX5dEtxER'#'jwbtzixyczrtbece'

manager = Manager(app)
mail = Mail(app)

if __name__ == '__main__':
    manager.run()
