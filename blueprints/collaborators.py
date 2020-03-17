from flask import Blueprint, Response, request

collaborators_blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/api/collaborators')

@collaborators_blueprint.route('/', methods=['GET'])
def collaborators():
    """
    Return all the collaborators with their respective first name, last name, collabID and email.
    """
    pass

@collaborators_blueprint.route('/ban', methods=['PUT'])
def collaborators_ban():
    """
    Ban a collaborator from the system
    """
    pass

@collaborators_blueprint.route('/unban', methods=['PUT'])
def collaborators_unban():
    """
    UnBan a collaborator from the system
    """
    pass
