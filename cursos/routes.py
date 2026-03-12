from flask import render_template, request, redirect, url_for
from flask import Blueprint
import forms
from models import db, Curso

cursos_bp = Blueprint('cursos', __name__)

@cursos_bp.route("/cursos")
def dashboardCurso():
    create_form = forms.CursosForm(request.form)
    cursos = Curso.query.all()
    return render_template("dashboardCurso.html", form=create_form, cursos=cursos)

@cursos_bp.route("/agregarCurso", methods=['GET','POST'])
def agregarCurso():
    create_form = forms.CursosForm(request.form)
    if request.method == 'POST':
        cur = Curso(nombre=create_form.nombre.data,
                    descripcion=create_form.descripcion.data,
                    maestro_id=create_form.maestro_id.data)
        db.session.add(cur)
        db.session.commit()
        return redirect(url_for('cursos.dashboardCurso'))
    return render_template("Cursos.html", form=create_form)

@cursos_bp.route("/modificarCurso", methods=['GET','POST'])
def modificarCurso():
    create_form = forms.CursosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = cur1.nombre
        create_form.descripcion.data = cur1.descripcion
        create_form.maestro_id.data = cur1.maestro_id
        
    if request.method == 'POST':
        id = create_form.id.data
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        cur1.nombre = create_form.nombre.data
        cur1.descripcion = create_form.descripcion.data
        cur1.maestro_id = create_form.maestro_id.data
        db.session.commit()
        return redirect(url_for('cursos.dashboardCurso'))
    return render_template("modificarCurso.html", form=create_form)

@cursos_bp.route("/eliminarCurso", methods=['GET','POST'])
def eliminarCurso():
    create_form = forms.CursosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = cur1.nombre
        create_form.descripcion.data = cur1.descripcion
        create_form.maestro_id.data = cur1.maestro_id
        
    if request.method == 'POST':
        id = create_form.id.data
        cur1 = Curso.query.get(id)
        db.session.delete(cur1)
        db.session.commit()
        return redirect(url_for('cursos.dashboardCurso'))
    return render_template("eliminarCurso.html", form=create_form)

@cursos_bp.route("/detallesCurso", methods=['GET'])
def detallesCurso():
    id = request.args.get('id')
    cur1 = Curso.query.get(id)
    return render_template("detallesCurso.html", curso=cur1)