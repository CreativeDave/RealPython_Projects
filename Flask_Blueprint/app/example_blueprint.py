from flask import Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return "this is an example app with a flask blueprint"
