from flask_wtf import FlaskForm
import phonenumbers
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError 




class PhoneForm(FlaskForm):
    username = StringField('Avenger Name:', validators = [DataRequired()])
    phonenumber = StringField('Phone Number:', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumbersutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


