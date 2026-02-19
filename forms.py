from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, EmailField, validators, RadioField
from flask_wtf import FlaskForm

class UserForms(Form):
    matricula=IntegerField('Id')
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese nombre valido")])
    apaterno=StringField('Apaterno',[
        validators.DataRequired(message="El campo es requerido")])
    correo=EmailField('Correo' ,[
        validators.DataRequired(message="El campo es requerido")])

class CineForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    compradores = IntegerField('Cant. Compradores', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message='Debe haber al menos 1 comprador')
    ])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('Si','Si'), ('No','No')], default='No')
    boletas = IntegerField('Cant. Boletos', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message='Debe haber al menos 1 boleto')
    ])


    