from wtforms import Form
from wtforms import Form, StringField, IntegerField, PasswordField, EmailField, validators, RadioField, SelectField
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
        validators.Email(message="Ingrese un correo valido")])

class MaestrosForm(Form):
    matricula = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido")])
    apellidos = StringField('Apellidos',[
        validators.DataRequired(message="Este campo es requerido")])
    especialidad = StringField('Especialidad',[
        validators.DataRequired(message="Este campo es requerido")])
    correo = EmailField('Correo',[
        validators.DataRequired(message="Este campo es requerido")])

class CursosForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre', [validators.DataRequired(message="Este campo es requerido")])
    descripcion = StringField('Descripción', [validators.DataRequired(message="Este campo es requerido")])
    maestro_id = IntegerField('Matrícula del Maestro', [
        validators.DataRequired(message="Este campo es requerido (Debe existir en Maestros)")
    ])
    curso_id = SelectField('Curso', coerce=int, validators=[
        validators.DataRequired(message="Seleccione un curso")
    ])

class InscripcionForm(Form):
    id = IntegerField('Id')
    alumno_id = SelectField('Alumno', coerce=int, validators=[validators.DataRequired()])
    curso_id = SelectField('Curso', coerce=int, validators=[validators.DataRequired()])
    