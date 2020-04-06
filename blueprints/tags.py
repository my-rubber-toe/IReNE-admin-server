from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from utils.validators import ObjectID
from daos.tags import TagsDAO

blueprint = Blueprint('tags', __name__, url_prefix='/admin/tags')
dao = TagsDAO()
@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def tags():
    """
    Retrieve a list of all the system tags.
    """
    # TODO: Use DAOs to retrieve all the tags.
    return ApiResult( body = 
        {'tags': dao.get_tags()}
    )

@blueprint.route('/remove', methods=['PUT'])
@fresh_jwt_required
def tags_remove():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    tagID  = request.form.get('tagID')
    if not ObjectID().is_valid(tagID):
        raise AdminServerApiError(
            msg='The tag ID given is not valid.',
            status=404
        )

    tag = dao.remove_tag(tagID)
    if tag is None:
        raise AdminServerApiError(
            msg='The tag ID given was not found.',
            status=404
        )
    return ApiResult(body = 
        {'tag': tag}
    )