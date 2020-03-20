from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required

blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/api/collaborators')

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def collaborators():
    """
    Return all the collaborators with their respective first name, last name, collabID and email.
    """
    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data'
    )

@blueprint.route('/ban', methods=['PUT'])
@fresh_jwt_required
def collaborators_ban():
    """
    Ban a collaborator from the system
    """
    #collab_id  = request.form.get('collabID')
    #valid_collab_id = ObjectID().is_valid(collab_id)
    valid_collab_id = False
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given was not validated.',
            status=400
        )
    collab_id_exist = False
    # TODO: Check if collab id exist
    if not collab_id_exist:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )


    # TODO: Use DAOs to ban collaborator.
    # TODO: Unpublish all collaborators documents.
    return ApiResult(
        message='Valid Collaborator Ban'
    )

@blueprint.route('/unban', methods=['PUT'])
@fresh_jwt_required
def collaborators_unban():
    """
    UnBan a collaborator from the system
    """
    #collab_id  = request.form.get('collabID')

    #valid_collab_id = ObjectID().is_valid(collab_id)
    valid_collab_id = False
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given was not validated.',
            status=400
        )
    collab_id_exist = False
    # TODO: Check if collab id exist
    if not collab_id_exist:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )
    # TODO: Use DAOs to unban collaborator.
    # TODO: Publish all collaborators documents.
    return ApiResult(
        message='Valid Collaborator Ban'
    )
