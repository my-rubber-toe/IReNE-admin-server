"""
documents.py
====================================
Every route regarding documents, including publishing or unpublishing a document and seeing all of current documents in the systen can be found here.
"""
from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.documents_dao import DocumentsDAO
from utils.validators import objectId_is_valid
import json

blueprint = Blueprint('documents', __name__, url_prefix='/admin/documents')
dao = DocumentsDAO()

@blueprint.route('/', methods=['GET'])
@fresh_jwt_required
def documents():
    """
    Retrieve a list of all the documents in the database.
    Returns
    -------
    Document[]
        List of collaborators currently in the system.
    """
    documents = dao.get_all_documents()
    return ApiResult(
        body={'documents': json.loads(documents.to_json())}
    )

@blueprint.route('/view/<docID>', methods=['GET'])
@fresh_jwt_required
def documents_view(docID):
    """
    Retrieve a list of metadata of all the documents in the database.
    """
    valid_doc_id = objectId_is_valid(docID)
    if not valid_doc_id:
        raise AdminServerApiError(
            msg='The documents ID given is not valid.',
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
    Pusblish a document. 
    
    Parameters
    ----------
    docID : ObjectId
        12-byte MongoDB compliant Object id of the document to be publish.
    
    Returns
    -------
    Document
        Document that has been published.
    
    Raises
    ------
    AdminServerApiError
        If the document id is not valid or if a document with the given id was not found.

    """
    doc_id  = request.form.get('docID')
    valid_doc_id = objectId_is_valid(doc_id)
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
    Unpusblish a document. 
    
    Parameters
    ----------
    docID : ObjectId
        12-byte MongoDB compliant Object id of the document to be unpublish.
    
    Returns
    -------
    Document
        Document that has been unpublished.
    
    Raises
    ------
    AdminServerApiError
        If the document id is not valid or if a document with the given id was not found.

    """
    doc_id  = request.form.get('docID')
    valid_doc_id = objectId_is_valid(doc_id)
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