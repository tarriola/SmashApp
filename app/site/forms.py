from flask_wtf import Form

from wtforms import TextField

#from wtforms.validators import Required

class AddForm(Form):
    name = TextField('name')

    info = TextField('info')
