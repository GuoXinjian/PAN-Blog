from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField
from wtforms.validators import DataRequired,Length,Email,Regexp
from wtforms import ValidationError
from ..models import Role, User

class NameForm(FlaskForm):
    name   = StringField('姓名',validators=[DataRequired()])
    submit = SubmitField('确定')








