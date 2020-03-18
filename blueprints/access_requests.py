from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException

blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/api/access-request')

@blueprint.route('/', methods=['GET'])
def access_requests():
    """
    Retrieve the list of access requests from the database.
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

@blueprint.route('/approve', methods=['PUT'])
def access_requests_approve():
    """
    Approve the access request of a user. 
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

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data'
    )

@blueprint.route('/deny', methods=['DELETE'])
def access_requests_deny():
    """
    Deny the access request of a user. 
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

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data'
    )