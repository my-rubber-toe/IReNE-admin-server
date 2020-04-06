from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.documents import DocumentsDAO
from utils.validators import ObjectID

blueprint = Blueprint('documents', __name__, url_prefix='/admin/documents')
dao = DocumentsDAO()

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def documents():
    """
    Retrieve a list of all the documents in the database.
    """
    return ApiResult(
        body={'documents':dao.get_all_documents()}
    )

@blueprint.route('/view/<docID>', methods=['GET'])
@fresh_jwt_required
def documents_view(docID):
    """
    Retrieve a list of metadata of all the documents in the database.
    """
    valid_doc_id = ObjectID().is_valid(docID)
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given was not validated.',
            status=400
        )
    document = dao.get_document(docID)
    if not document:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )
    return ApiResult( body = 
        {'document': document}
    )

@blueprint.route('/publish', methods=['PUT'])
@fresh_jwt_required
def documents_publish():
    """
    Set a document state to be pusblished.
    """
    doc_id  = request.form.get('docID')
    valid_doc_id = ObjectID().is_valid(doc_id)
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given is not valid.',
            status=400
        )
    document = dao.publish_document(doc_id)
    if not document:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )
    return ApiResult( body =
        {'document': document}
    )

@blueprint.route('/unpublish', methods=['PUT'])
@fresh_jwt_required
def documents_unpublish():
    """
    Set a document state to be unpublished.
    """
    doc_id  = request.form.get('docID')
    valid_doc_id = ObjectID().is_valid(doc_id)
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given is not valid.',
            status=400
        )
    document = dao.unpublish_document(doc_id)
    if not document:
        raise AdminServerApiError(
            msg='The documents ID given was not found.',
            status=404
        )
    return ApiResult( body =
        {'document': document}
    )