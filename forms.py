from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, EmailField, validators, RadioField
from flask_wtf import FlaskForm

class UserForm2(Form):
    id = IntegerField('Id') 
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese nombre valido")])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido")])
    telefono = StringField('Telefono', [
        validators.DataRequired(message="El campo es requerido")])
    correo = EmailField('Correo', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

class MaestrosForm(Form):
    matricula = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    apellidos = StringField('Apellidos',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    especialidad = StringField('Especialidad',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    correo = EmailField('Correo',[
        validators.DataRequired(message="Este campo es requerido")
    ])




    