from flask import Blueprint, Response, request
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from utils.responses import ApiResult, ApiException
from utils.validators import ObjectID
from exceptions.handler import AdminServerApiError, AdminServerAuthError

blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/access-request')

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def access_requests():
    """
    Retrieve the list of access requests from the database.
    """
    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data'
    )

@blueprint.route('/approve', methods=['PUT'])
@fresh_jwt_required
def access_requests_approve():
    """
    Approve the access request of a user. 
    """
    collab_id  = request.form.get('collabID')
    #valid_collab_id = ObjectID().is_valid(collab_id)
    valid_collab_id = True
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given was not validated.',
            status=400
        )
    collab_id_exist = True
    # TODO: Check if collab id exist
    if not collab_id_exist:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data',
        collabID = collab_id
    )

@blueprint.route('/deny', methods=['DELETE'])
@fresh_jwt_required
def access_requests_deny():
    """
    Deny the access request of a user. 
    """
    collab_id  = request.form.get('collabID')
    #valid_collab_id = ObjectID().is_valid(collab_id)
    valid_collab_id = True
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given was not validated.',
            status=400
        )
    # TODO: Check if collab id exist
    collab_id_exist = True
    # TODO: Check if collab id exist
    if not collab_id_exist:
        return AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        message='Valid Data',
        collabID = collab_id
    )