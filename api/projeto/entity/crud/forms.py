# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from projeto.entity.document.model import Document

class RegisterForm(FlaskForm):
    
     NM_NUMERO_DOCUMENTO = StringField(
        "número do documento", validators=[DataRequired(), Length(min=3, max=25)]
    )
   
   
def __init__(self, *args, **kwargs):
    """Create instance."""
    super(RegisterForm, self).__init__(*args, **kwargs)
    self.user = None




