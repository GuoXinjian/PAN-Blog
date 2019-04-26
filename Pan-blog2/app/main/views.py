from datetime import datetime
from flask import render_template, session, redirect, url_for,send_from_directory
import os

from . import main 
from .forms import NameForm
from .. import db 
from ..models import User

@main.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ....
        return redirect(url_for('.index'))
    return render_template('index.html',
                            form=form,name=session.get('name'),
                            known=session.get('known',False),
                            current_time=datetime.utcnow())


# @main.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(main.root_path,'static'),'favicon.ico' , mimetype='imge/vnd.microsoft.icon')