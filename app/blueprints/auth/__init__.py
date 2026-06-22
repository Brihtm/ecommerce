from flask import Blueprint

auth_bp = Blueprint(
    'public', 
    __name__, 
    template_folder='../../template_folder/public'
)

from . import routes