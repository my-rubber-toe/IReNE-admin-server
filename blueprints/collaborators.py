from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.collaborators import CollaboratorsDAO
from utils.validators import ObjectID

blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/collaborators')
dao =  CollaboratorsDAO()
@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def collaborators():
    """
    Return all the collaborators with their respective first name, last name, collabID and email.
    """
    # TODO: Use DAOs to retrieve the necessary information.
    collaborators = dao.get_collaborators()
    return ApiResult(
        body={'collaborators':collaborators}
    )

@blueprint.route('/ban', methods=['PUT'])
@fresh_jwt_required
def collaborators_ban():
    collab_id  = request.form.get('collabID')
    valid_collab_id = ObjectID().is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given is not valid.',
            status=400
        )
    collaborator = dao.ban_collaborator(collab_id)
    if collaborator is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(body = 
        {'collaborator': collaborator}
    )

@blueprint.route('/unban', methods=['PUT'])
@fresh_jwt_required
def collaborators_unban():
    """
    Approve the access request of a user. 
    """
    collab_id  = request.form.get('collabID')
    valid_collab_id = ObjectID().is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given is not valid.',
            status=400
        )
    collaborator = dao.unban_collaborator(collab_id)
    if collaborator is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )
    return ApiResult(body = 
        {'collaborator': collaborator}
    )