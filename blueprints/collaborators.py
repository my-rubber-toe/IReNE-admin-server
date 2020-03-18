from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException

blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/api/collaborators')

@blueprint.route('/', methods=['GET'])
def collaborators():
    """
    Return all the collaborators with their respective first name, last name, collabID and email.
    """
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        return ApiException(
            error_type='Unauthorized',
            message='Unauthorized access to admin dashboard.',
            status=401
        )
    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data'
    )

@blueprint.route('/ban', methods=['PUT'])
def collaborators_ban():
    """
    Ban a collaborator from the system
    """
    #collab_id  = request.form.get('collabID')
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        return ApiException(
            error_type='Unauthorized',
            message='Unauthorized access to admin dashboard.',
            status=401
        )
    
    valid_collab_id = False
    # TODO: Check if collab id exist
    if not valid_collab_id:
        return ApiException(
            error_type='Not Found',
            message='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to ban collaborator.
    # TODO: Unpublish all collaborators documents.
    return ApiResult(
        message='Valid Collaborator Ban'
    )

@blueprint.route('/unban', methods=['PUT'])
def collaborators_unban():
    """
    UnBan a collaborator from the system
    """
    #collab_id  = request.form.get('collabID')
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        return ApiException(
            error_type='Unauthorized',
            message='Unauthorized access to admin dashboard.',
            status=401
        )
    
    valid_collab_id = False
    # TODO: Check if collab id exist
    if not valid_collab_id:
        return ApiException(
            error_type='Not Found',
            message='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to unban collaborator.
    # TODO: Publish all collaborators documents.
    return ApiResult(
        message='Valid Collaborator Ban'
    )
