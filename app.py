from flask import Flask, render_template, request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

from models import db
from models import Alumnos

from flask_migrate import Migrate

from maestros.routes import maestros_bp
from cursos.routes import cursos_bp
from inscripciones.routes import inscripciones_bp



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect()

migrate = Migrate(app, db)

app.register_blueprint(maestros_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(inscripciones_bp)


@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/dashboardAlumno", methods=["GET"])
def dashboardAlumno():
    alumnos = Alumnos.query.all()
    return render_template("dashboardAlumno.html", alumnos=alumnos)


@app.errorhandler(404)
def page_not_fount(e):
	return render_template("404.html")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
	create_form=forms.UserForm2(request.form)
	if request.method=='POST':
		alum=Alumnos(nombre=create_form.nombre.data,
                       apellidos=create_form.apellidos.data,
                       telefono=create_form.telefono.data,
                       correo=create_form.correo.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("alumnos.html", form=create_form)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            create_form.id.data = alum1.id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.telefono.data = alum1.telefono
            create_form.correo.data = alum1.correo
            
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            alum1.nombre = create_form.nombre.data
            alum1.apellidos = create_form.apellidos.data
            alum1.telefono = create_form.telefono.data
            alum1.correo = create_form.correo.data
            db.session.commit() 
            return redirect(url_for('index'))
            
    return render_template("modificar.html", form=create_form)

@app.route("/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    if not alum1:
        return redirect(url_for('index')) # Si no existe, regresa al index
        
    return render_template("detalles.html", 
                           nombre=alum1.nombre, 
                           apellidos=alum1.apellidos, 
                           telefono=alum1.telefono,
                           correo=alum1.correo)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm2(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        if not alum1:
            return redirect(url_for('index'))
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.telefono.data = alum1.telefono
        create_form.correo.data = alum1.correo
        return render_template("eliminar.html", form=create_form)
        
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            db.session.delete(alum1)
            db.session.commit()
        return redirect(url_for('index'))



if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()

	app.run()
