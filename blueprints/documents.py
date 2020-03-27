from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required

blueprint = Blueprint('documents', __name__, url_prefix='/admin/documents')

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def documents():
    """
    Retrieve a list of all the documents in the database.
    """
    # TODO: Use DAOs to retrieve all the documents.
    return ApiResult(
        message='Documents'
    )

@blueprint.route('/view/<docID>', methods=['GET'])
@fresh_jwt_required
def documents_view(docID):
    """
    Retrieve a list of metadata of all the documents in the database.
    """
    #valid_doc_id = ObjectID().is_valid(docID)
    valid_doc_id = True
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = True
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to retrieve document.
    return ApiResult(
        message='Valid Document View',
        docID = docID
    )

@blueprint.route('/publish', methods=['PUT'])
@fresh_jwt_required
def documents_publish():
    """
    Set a document state to be pusblished.
    """
    doc_id  = request.form.get('docID')
    #valid_doc_id = ObjectID().is_valid(doc_id)
    valid_doc_id = True
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = True
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to publish document.
    return ApiResult(
        message='Valid Document Publish',
        docID = doc_id
    )

@blueprint.route('/unpublish', methods=['PUT'])
@fresh_jwt_required
def documents_unpublish():
    """
    Set a document state to be unpublished.
    """
    doc_id  = request.form.get('docID')
    #valid_doc_id = ObjectID().is_valid(doc_id)
    valid_doc_id = True
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    doc_id_exist = True
    # TODO: Check if doc id exist
    if not doc_id_exist:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )

    # TODO: Use DAOs to unpublish document.
    return ApiResult(
        message='Valid Document Unpublish',
        docID = doc_id
    )