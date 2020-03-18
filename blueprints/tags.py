from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException

blueprint = Blueprint('tags', __name__, url_prefix='/admin/api/tags')

@blueprint.route('/', methods=['GET'])
def tags():
    """
    Retrieve a list of all the system tags.
    """
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        return ApiException(
            error_type='Unauthorized',
            message='Unauthorized access to admin dashboard.',
            status=401
        )
    # TODO: Use DAOs to retrieve all the tags.
    return ApiResult(
        message='All available tags'
    )

@blueprint.route('/remove', methods=['DELETE'])
def tags_remove():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    #tag  = request.form.get('tag')
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        return ApiException(
            error_type='Unauthorized',
            message='Unauthorized access to admin dashboard.',
            status=401
        )
    
    valid_tag = False
    # TODO: Check if tag exist
    if not valid_tag:
        return ApiException(
            error_type='Not Found',
            message='The tag given was not found.',
            status=404
        )

    # TODO: Use DAOs to delete tag.
    return ApiResult(
        message='Valid Tga Deletion'
    )