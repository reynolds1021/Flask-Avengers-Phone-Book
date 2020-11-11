from flask_wtf import FlaskForm
import phonenumbers
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired




class PhoneForm(FlaskForm):
    first_name = StringField('First Name:', validators = [DataRequired()])
    last_name = StringField('Last Name:', validators = [DataRequired()])
    hero_name = StringField('Hero Name:', validators = [DataRequired()])
    address = StringField('Address:', validators = [DataRequired()])
    phone_number = StringField('Phone Number:', validators = [DataRequired()])
    submit = SubmitField('Submit:')

    

