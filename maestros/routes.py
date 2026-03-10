from flask import Blueprint
maestros_bp=Blueprint('maestros',__name__)

@maestros_bp.route('/maestros')
def maestros():
    return "Maestros"
