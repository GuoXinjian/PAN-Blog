# from flask_mail import Message
# from hello import *
#
# # app = Flask(__name__)
# msg=Message('My Subject',sender='851834378@qq.com',recipients=['780862850@qq.com'])
# msg.body='text body'
# msg.html='<b>HTML</b> body'
#
# with app.app_context():
#     mail.send(msg)


from hello import mail
from flask_mail import Message
from hello import *
from flask import current_app
msg = Message('Test mail', sender='851834378@qq.com',recipients=['780862850@qq.com'])
msg.body = 'text body'
msg.html = '<b>liuzhen</b> body111111'
# app_ctx = app.app_context()
# app_ctx.push()
# with app_ctx:
with app.app_context():
    mail.send(msg)

