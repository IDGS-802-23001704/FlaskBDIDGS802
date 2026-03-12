from flask import render_template, request, redirect, url_for, Blueprint
from models import db, Inscripcion, Alumnos, Curso
import forms

inscripciones_bp = Blueprint('inscripciones', __name__)

@inscripciones_bp.route("/inscripciones")
def dashboardInscripcion():
    inscripciones = Inscripcion.query.all()
    alumnos_dict = {a.id: f"{a.nombre} {a.apellidos}" for a in Alumnos.query.all()}
    cursos_dict = {c.id: c.nombre for c in Curso.query.all()}
    return render_template("dashboardInscripcion.html", inscripciones=inscripciones, alumnos_dict=alumnos_dict, cursos_dict=cursos_dict)

@inscripciones_bp.route("/inscribir", methods=['GET', 'POST'])
def inscribir():
    create_form = forms.InscripcionForm(request.form)
    create_form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apellidos}") for a in Alumnos.query.all()]
    create_form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]

    if request.method == 'GET':
        if 'alumno_id' in request.args:
            create_form.alumno_id.data = int(request.args.get('alumno_id'))

    if request.method == 'POST':
        alumno = Alumnos.query.get(create_form.alumno_id.data)
        curso = Curso.query.get(create_form.curso_id.data)
        
        if alumno and curso and alumno not in curso.alumnos:
            curso.alumnos.append(alumno)
            db.session.commit()
        return redirect(url_for('inscripciones.dashboardInscripcion'))

    return render_template("inscribir.html", form=create_form)



@inscripciones_bp.route("/eliminarInscripcion", methods=['GET', 'POST'])
def eliminarInscripcion():
    create_form = forms.InscripcionForm(request.form)
    
    if request.method == 'GET':
        id_insc = request.args.get('id')
        inscripcion = Inscripcion.query.get(id_insc)
        if not inscripcion:
            return redirect(url_for('inscripciones.dashboardInscripcion'))
            
        create_form.id.data = inscripcion.id
        create_form.alumno_id.choices = [(inscripcion.alumno_id, str(inscripcion.alumno_id))]
        create_form.curso_id.choices = [(inscripcion.curso_id, str(inscripcion.curso_id))]
        return render_template("eliminarInscripcion.html", form=create_form, inscripcion=inscripcion)

    if request.method == 'POST':
        id_insc = create_form.id.data
        inscripcion = Inscripcion.query.get(id_insc)
        if inscripcion:
            db.session.delete(inscripcion)
            db.session.commit()
        return redirect(url_for('inscripciones.dashboardInscripcion'))