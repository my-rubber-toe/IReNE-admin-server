"""
collaborators.py
====================================
Every route regarding collaborators, including but not limited to banning or unbanning a collaborator and seeing all of current collaborators in the systen can be found here.
"""
from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.collaborators_dao import CollaboratorsDAO
from daos.admin_dao import AdminDAO
from utils.validators import objectId_is_valid
import json


blueprint = Blueprint('collaborators', __name__, url_prefix='/admin/collaborators')
dao =  CollaboratorsDAO()
daoAdmin = AdminDAO()

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def collaborators():
    """
    Retrieve a list of approved collaborators from the database.

    Returns
    -------
    Collaborator[]
        List of collaborators currently in the system.
    """
    collaborators = dao.get_collaborators()
    return ApiResult(
        body={'collaborators': json.loads(collaborators)}
    )

@blueprint.route('/ban', methods=['PUT'])
@fresh_jwt_required
def collaborators_ban():
    """
    Ban a collaborator. 
    
    Parameters
    ----------
    collabID : ObjectId
        12-byte MongoDB compliant Object id of the collaborator to be banned.
    
    Returns
    -------
    Collaborator
        Collaborator that has been banned.
    
    Raises
    ------
    AdminServerApiError
        If the collaborators id is not valid or if a collaborator with the given id was not found.

    """
    collab_id = request.form.get('collabID')
    password = request.form.get('password')
    valid_collab_id = objectId_is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given is not valid.',
            status=400
        )
    if not daoAdmin.check_password(daoAdmin.get_admin(get_jwt_identity()).password, password):
        raise AdminServerApiError(
            msg='The password given was does not match our records.',
            status=403
        )
    collaborator = dao.ban_collaborator(collab_id)
    if collaborator is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )

    return ApiResult(body = 
        {'collaborator': collab_id}
    )

@blueprint.route('/unban', methods=['PUT'])
@fresh_jwt_required
def collaborators_unban():
    """
    Unban a collaborator. 
    
    Parameters
    ----------
    collabID : ObjectId
        12-byte MongoDB compliant Object id of the collaborator to be unbanned.
    
    Returns
    -------
    Collaborator
        Collaborator that has been unbanned.
    
    Raises
    ------
    AdminServerApiError
        If the collaborators id is not valid or if a collaborator with the given id was not found.

    """
    collab_id  = request.form.get('collabID')
    password = request.form.get('password')
    valid_collab_id = objectId_is_valid(collab_id)
    if not valid_collab_id:
        raise AdminServerApiError(
            msg='The collaborators ID given is not valid.',
            status=400
        )
    if not daoAdmin.check_password(daoAdmin.get_admin(get_jwt_identity()).password, password):
        raise AdminServerApiError(
            msg='The password given was does not match our records.',
            status=403
        )
    collaborator = dao.unban_collaborator(collab_id)
    if collaborator is None:
        raise AdminServerApiError(
            msg='The collaborators ID given was not found.',
            status=404
        )
    return ApiResult(body = 
        {'collaborator': collab_id}
    )