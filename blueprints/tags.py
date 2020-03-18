from flask import Blueprint, Response, request

blueprint = Blueprint('tags', __name__, url_prefix='/admin/api/tags')

@blueprint.route('/', methods=['GET'])
def tags():
    """
    Retrieve a list of all the system tags.
    """
    return "Tags"

@blueprint.route('/remove', methods=['DELETE'])
def tags_remove():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    return "Removed tag"