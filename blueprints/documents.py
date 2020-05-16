"""
documents.py
====================================
Every route regarding documents, including publishing or unpublishing a document and seeing all of current documents in the systen can be found here.
"""
from flask import Blueprint, request, current_app
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.documents_dao import DocumentsDAO
from daos.collaborators_dao import CollaboratorsDAO
from daos.admin_dao import AdminDAO
from utils.validators import objectId_is_valid
import json

blueprint = Blueprint('documents', __name__, url_prefix='/documents')
dao = DocumentsDAO()
daoCollab = CollaboratorsDAO()
daoAdmin = AdminDAO()


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
        body={'documents': json.loads(documents)}
    )


@blueprint.route('/view/<docID>', methods=['GET'])
@fresh_jwt_required
def documents_view(docID):
    """
    Returns a document to view. 
    
    Parameters
    ----------
    docID : ObjectId
        12-byte MongoDB compliant Object id of the document to be publish.
    
    Returns
    -------
    Document
        Document that is going to be viewed.
    
    ApiException
        If the document id is not valid or if a document with the given id was not found.

    """
    valid_doc_id = objectId_is_valid(docID)
    if not valid_doc_id:
        return ApiException(
            error_type = "Validation Error",
            message='The documents ID given is not valid.',
            status=400
        )
    document = dao.get_document(docID)
    if not document:
        return ApiException(
            error_type = "Database Error",
            message='The documents ID given was not found.',
            status=404
        )
    collab = document.creatoriD
    actors = []
    authors = []
    sections = []
    for author in document.author:
        authors.append(json.loads(author.to_json()))
    for actor in document.actor:
        actors.append(json.loads(actor.to_json()))
    for section in document.section:
        sections.append(json.loads(section.to_json()))
    body = {
        '_id': str(document.id),
        'title': document.title,
        'description': document.description,
        'creatorFullName': collab.first_name + " " + collab.last_name,
        'creatorEmail': collab.email,
        'creationDate': document.creationDate,
        'lastModificationDate': document.lastModificationDate,
        'incidentDate': document.incidentDate,
        'tagsDoc': document.tagsDoc,
        'infrasDocList': document.infrasDocList,
        'damageDocList': document.damageDocList,
        'author': authors,
        'actor': actors,
        'section': sections
    }
    body = json.dumps(body)
    return ApiResult(body=
                     {'document': json.loads(body)}
                     )


@blueprint.route('/publish', methods=['PUT'])
@fresh_jwt_required
def documents_publish():
    """
    Publish a document. 
    
    Parameters
    ----------
    docID : ObjectId
        12-byte MongoDB compliant Object id of the document to be publish.
    
    Returns
    -------
    ObjectID
        ObjectID of the document that was published.
    
    ApiException
        If the document id is not valid or if a document with the given id was not found.

    """
    doc_id  = request.form.get('docID')
    password = request.form.get('password')
    valid_doc_id = objectId_is_valid(doc_id)
    if not valid_doc_id:
        return ApiException(
            error_type = "Validation Error",
            message='The documents ID given is not valid.',
            status=400
        )
    if not daoAdmin.check_password(daoAdmin.get_admin(get_jwt_identity()).password, password):
        return ApiException(
            error_type = "Authentication Error",
            message='The password given was does not match our records.',
            status=403
        )
    document = dao.publish_document(doc_id)
    if not document:
        return ApiException(
            error_type = "Database Error",
            message='The documents ID given was not found.',
            status=404
        )
    return ApiResult(body={'docID': doc_id})


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
    ObjectID
        ObjectID of the document that was unpublished.
    
    ApiException
        If the document id is not valid or if a document with the given id was not found.

    """
    doc_id  = request.form.get('docID')
    password = request.form.get('password')
    valid_doc_id = objectId_is_valid(doc_id)
    if not valid_doc_id:
        return ApiException(
            error_type = "Validation Error",
            message='The documents ID given is not valid.',
            status=400
        )
    if not daoAdmin.check_password(daoAdmin.get_admin(get_jwt_identity()).password, password):
        return ApiException(
            error_type = "Authentication Error",
            message='The password given  does not match our records.',
            status=403
        )
    document = dao.unpublish_document(doc_id)
    if not document:
        return ApiException(
            error_type = "Database Error",
            message='The documents ID given was not found.',
            status=404
        )
    return ApiResult(body=
                     {'docID': doc_id}
                     )