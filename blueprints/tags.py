from flask import Blueprint, Response, request

tags_blueprint = Blueprint('tags', __name__, url_prefix='/admin/api/tags')

@tags_blueprint.route('/', methods=['GET'])
def tags():
    """
    Retrieve a list of all the system tags.
    """
    pass

@tags_blueprint.route('/remove', methods=['DELETE'])
def tags():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    pass