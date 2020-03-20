from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError

blueprint = Blueprint('documents', __name__, url_prefix='/admin/api/documents')

@blueprint.route('/', methods=['GET'])
def documents():
    """
    Retrieve a list of all the documents in the database.
    """
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    # TODO: Use DAOs to retrieve all the documents.
    return ApiResult(
        message='All available documents'
    )

@blueprint.route('/view/<docID>', methods=['GET'])
def documents_view(docID):
    """
    Retrieve a list of metadata of all the documents in the database.
    """
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    #valid_doc_id = ObjectID().is_valid(docID)
    valid_doc_id = False
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = False
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve document.
    return ApiResult(
        message='Valid Collaborator Ban'
    )

@blueprint.route('/publish', methods=['PUT'])
def documents_publish():
    """
    Set a document state to be pusblished.
    """
    #doc_id  = request.form.get('docID')
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    
    #valid_doc_id = ObjectID().is_valid(doc_id)
    valid_doc_id = False
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = False
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to publish document.
    return ApiResult(
        message='Valid Document Publish'
    )

@blueprint.route('/unpublish', methods=['PUT'])
def documents_unpublish():
    """
    Set a document state to be unpublished.
    """
    #doc_id  = request.form.get('docID')
    valid_session_token = False
    # TODO: Check if user has a valid session token.
    if not valid_session_token:
        raise AdminServerAuthError(
            msg= 'Unauthorized access to admin dashboard.', 
            status = 401
            )
    
    #valid_doc_id = ObjectID().is_valid(doc_id)
    valid_doc_id = False
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = False
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to unpublish document.
    return ApiResult(
        message='Valid Document Unpublish'
    )