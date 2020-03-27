from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required

blueprint = Blueprint('tags', __name__, url_prefix='/admin/api/tags')

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def tags():
    """
    Retrieve a list of all the system tags.
    """
    # TODO: Use DAOs to retrieve all the tags.
    return ApiResult(
        message='All available tags'
    )

@blueprint.route('/remove', methods=['DELETE'])
@fresh_jwt_required
def tags_remove():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    tag_name  = request.form.get('tagName')
    valid_tag = True
    # TODO: Check if tag exist
    if not valid_tag:
        raise AdminServerApiError(
            msg='The tag given was not found.',
            status=404
        )

    # TODO: Use DAOs to delete tag.
    return ApiResult(
        message='Valid Tag Deletion',
        tagName = tag_name
    )