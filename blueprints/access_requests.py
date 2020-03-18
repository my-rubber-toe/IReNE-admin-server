from flask import Blueprint, Response, request

blueprint = Blueprint('access-requests', __name__, url_prefix='/admin/api/access-request')

@blueprint.route('/', methods=['GET'])
def access_requests():
    """
    Retrieve the list of access requests from the database.
    """
    # TODO: Check if user has a valid session token.
    return "Access Request"
"""
    try:
        GetDocumentsValidator().load(request.json)
    except ValidationError as err:
        return ApiException(
            error_type='Validation Error',
            message=err.messages,
            status=400
        )

    # TODO: Use DAOs to retrieve the necessary information.

    return ApiResult(
        message='Valid Data'
    )"""

@blueprint.route('/approve', methods=['PUT'])
def access_requests_approve():
    """
    Approve the access request of a user. 
    """
    return "Access Request Approve"

@blueprint.route('/deny', methods=['DELETE'])
def access_requests_deny():
    """
    Deny the access request of a user. 
    """
    return "Access Request Deny"