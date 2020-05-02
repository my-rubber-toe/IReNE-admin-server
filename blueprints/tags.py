"""
tags.py
====================================
Every route regarding tags, including removing a tag and seeing all of current tags in the systen can be found here.
"""
from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from utils.validators import objectId_is_valid
from daos.tags_dao import TagsDAO
import json

blueprint = Blueprint('tags', __name__, url_prefix='/admin/tags')
dao = TagsDAO()
@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def tags():
    """
    Retrieve a list of all the system tags.
    Returns
    -------
    Tag[]
        List of tags currently in the system.
    """
    tags = dao.get_tags()
    body = []
    for tag in tags:
        body.append({
            '_id': str(tag['_id']['$oid']),
            'tagItem': tag['tagItem']
        })
    body = json.dumps(body)
    return ApiResult( body = 
        {'tags': json.loads(body)}
    )

@blueprint.route('/remove', methods=['PUT'])
@fresh_jwt_required
def tags_remove():
    """
    Remove a tag from all documents and the system tags colleciton.
    """
    tagID  = request.form.get('tagID')
    if not objectId_is_valid(tagID):
        raise AdminServerApiError(
            msg='The tag ID given is not valid.',
            status=400
        )

    tag = dao.remove_tag(tagID)
    if tag is None:
        raise AdminServerApiError(
            msg='The tag ID given was not found.',
            status=404
        )
    return ApiResult(body = 
        {'tag': tagID}
    )