from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, EmailField, validators, RadioField
from flask_wtf import FlaskForm

class UserForm2(Form):
    id = IntegerField('Id') 
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese nombre valido")])
    apaterno=StringField('Apaterno',[
        validators.DataRequired(message="El campo es requerido")])
    email=EmailField('Correo' ,[
        validators.Email(message="Ingrese un correo valido")])




    