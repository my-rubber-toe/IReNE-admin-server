from flask import Blueprint, Response, request

access_req_blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/api/access-request')

@access_req_blueprint.route('/', methods=['GET'])
def access_requests():
    """
    Retrieve the list of access requests from the database.
    """
    pass

@access_req_blueprint.route('/approve', methods=['PUT'])
def access_requests_approve():
    """
    Approve the access request of a user. 
    """
    pass

@access_req_blueprint.route('/deny', methods=['DELETE'])
def access_requests_deny():
    """
    Deny the access request of a user. 
    """
    pass