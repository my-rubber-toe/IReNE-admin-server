"""
access_requests.py
====================================
Every route regarding access requests, including but not limited to accepting/denying and seeing can be found here.
Important to note that access request are treated as collaborators who have yet to be approved.
"""

from flask import Blueprint, Response, request
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from utils.responses import ApiResult, ApiException
from utils.validators import objectId_is_valid
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from daos.access_requests_dao import AccessRequestsDAO
import json

blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/access-request')
dao = AccessRequestsDAO()

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def access_requests():
    """
    Retrieve the list of access requests from the database.

    Returns
    -------
    Collaborator[]
        List of access request currently in the system.
    """
    requests = dao.get_access_requests()
    body = []
    for req in requests:
       body.append({
        "_id": str(req.id),
        "first_name": req.first_name,
        "last_name": req.last_name,
        "email": req.email,
        "banned": req.banned,
        "approved": req.approved
        })
    body = json.dumps(body)
    return ApiResult(
        body={'requests': json.loads(body)}
    )

@blueprint.route('/approve', methods=['PUT'])
@fresh_jwt_required
def access_requests_approve():
    """
    Approve the access request of a user. 
    
    Parameters
    ----------
    collabID : ObjectId
        12-byte MongoDB compliant Object id of the access request to be denied.
    
    Returns
    -------
    Collaborator
        Access request item that has been accepted.
    
    Raises
    ------
    AdminServerApiError
        If the access request id is not valid or if an access request with the given id was not found.

    """
    collab_id  = request.form.get('collabID')
    valid_collab_id = objectId_is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The access request ID given is not valid.',
            status=400
        )
    access_request = dao.accept_access_request(collab_id)
    if access_request is None:
        raise AdminServerApiError(
            msg='The access request ID given was not found.',
            status=404
        )
    return ApiResult(body = 
        {'access_request': collab_id}
    )

@blueprint.route('/deny', methods=['PUT'])
@fresh_jwt_required
def access_requests_deny():
    """
    Deny the access request of a user.
    
    Parameters
    ----------
    collabID : ObjectId
        12-byte MongoDB compliant Object id of the access request to be denied.
    
    Returns
    -------
    Collaborator
        Access request item that has been denied.
    
    Raises
    ------
    AdminServerApiError
        If the access request id is not valid or if an access request with the given id was not found.

    """
    collab_id  = request.form.get('collabID')
    valid_collab_id = objectId_is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The access request ID given is not valid.',
            status=400
        )
    access_request = dao.deny_access_request(collab_id)
    if access_request is None:
        raise AdminServerApiError(
            msg='The access request ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve the necessary information.
    return ApiResult(
        body = {'access_request': collab_id}
    )