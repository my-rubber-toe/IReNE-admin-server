from flask import Blueprint, Response, request
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from utils.responses import ApiResult, ApiException
from utils.validators import ObjectID
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from daos.access_requests import AccessRequestsDAO

blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/access-request')
dao = AccessRequestsDAO()

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def access_requests():
    """
    Retrieve the list of access requests from the database.
    """
    # TODO: Use DAOs to retrieve the necessary information.
    requests = dao.get_access_requests()
    return ApiResult(
        body={'requests':requests}
    )

@blueprint.route('/approve', methods=['PUT'])
@fresh_jwt_required
def access_requests_approve():
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
    access_request = dao.accept_access_request(collab_id)
    if access_request is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(body = 
        {'access_request': access_request}
    )

@blueprint.route('/deny', methods=['PUT'])
@fresh_jwt_required
def access_requests_deny():
    """
    Deny the access request of a user. 
    """
    collab_id  = request.form.get('collabID')
    valid_collab_id = ObjectID().is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given is not valid.',
            status=400
        )
    access_request = dao.deny_access_request(collab_id)
    if access_request is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        body = {'access_request': access_request}
    )