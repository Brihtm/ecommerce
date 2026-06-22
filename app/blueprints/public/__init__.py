from flask import blueprints
public_bp('public', __name__, templates_folder ='../../templates/public'
)

from . import routes