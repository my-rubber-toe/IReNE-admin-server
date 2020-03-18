from flask import Blueprint, Response, request

blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/api/collaborators')

@blueprint.route('/', methods=['GET'])
def collaborators():
    """
    Return all the collaborators with their respective first name, last name, collabID and email.
    """
    pass

@blueprint.route('/ban', methods=['PUT'])
def collaborators_ban():
    """
    Ban a collaborator from the system
    """
    pass

@blueprint.route('/unban', methods=['PUT'])
def collaborators_unban():
    """
    UnBan a collaborator from the system
    """
    pass
