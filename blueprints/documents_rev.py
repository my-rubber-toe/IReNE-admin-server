"""
documents.py
Every route regarding documents, including publishing or unpublishing a document and seeing all of current documents in the systen can be found here.
"""
from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.documents_rev_dao import RevDocumentsDAO
from daos.collaborators_dao import CollaboratorsDAO
from daos.documents_dao import DocumentsDAO
from utils.validators import objectId_is_valid
import json

blueprint = Blueprint('documents-rev', __name__, url_prefix='/admin/documents-hist')
dao = RevDocumentsDAO()
daoDocuments = DocumentsDAO()
daoCollaborators = CollaboratorsDAO()

@blueprint.route('/', methods=['POST'])
@fresh_jwt_required
def get_revision_with_params():
    sortField  = request.form.get('sortField')
    sortOrder  = request.form.get('sortOrder')
    filterVal  = request.form.get('filterVal')
    pageNumber  = request.form.get('pageNumber')
    pageSize  = request.form.get('pageSize')
    revisionHistory, length = dao.get_documents_revisions(sortField, sortOrder, filterVal, int(pageNumber), int(pageSize))
    body = []
    for revision in revisionHistory:
            body.append({
                "_id": str(revision.id),
                "revision_date": revision.revision_date,
                "document_title": revision.document_title,
                "creator_name": revision.creator_name,
                'revision_type': revision.revision_type,
                'revision_number': revision.revision_number,
                'creator_email': revision.creator_email
                })
    body = json.dumps(body)
    return ApiResult(
        body={'revision-history': json.loads(body),
        'revision-history-length': length}
    )

@blueprint.route('/revision', methods=['POST'])
@fresh_jwt_required
def get_revision():
    """
    Retrieve a list of all the documents in the database.
    Returns
    -------
    Document[]
        List of collaborators currently in the system.
    """
    revDocId = request.form.get('revDocId')
    revision = dao.get_document_rev(revDocId)
    if revision is None:
        raise AdminServerApiError(
            msg='The revision document ID given was not found.',
            status=404
        )
    
    body = {'new': revision.field_changed.new.to_json(),
            'old': revision.field_changed.old.to_json()}
    print(body)
    return ApiResult(
        body={'revision': body}
    )
=======
"""
documents.py
====================================
Every route regarding documents, including publishing or unpublishing a document and seeing all of current documents in the systen can be found here.
"""
from flask import Blueprint, Response, request
from utils.responses import ApiResult, ApiException
from exceptions.handler import AdminServerApiError, AdminServerAuthError
from flask_jwt_extended import get_jwt_identity, fresh_jwt_required
from daos.documents_rev_dao import RevDocumentsDAO
from daos.collaborators_dao import CollaboratorsDAO
from daos.documents_dao import DocumentsDAO
from utils.validators import objectId_is_valid
import json

blueprint = Blueprint('documents-rev', __name__, url_prefix='/admin/documents-hist')
dao = RevDocumentsDAO()
daoDocuments = DocumentsDAO()
daoCollaborators = CollaboratorsDAO()


@blueprint.route('/', methods=['GET', 'POST'])
@fresh_jwt_required
def documents_rev():
    """
    Retrieve a list of all the documents in the database.
    Returns
    -------
    Document[]
        List of collaborators currently in the system.
    """
    documents_rev = dao.get_all_documents_rev()
    body = []
    for revDoc in documents_rev:
        collab = daoCollaborators.get_collab(str(revDoc.creatorId))
        document = daoDocuments.get_document(str(revDoc.docId))
        name = collab.first_name + " " + collab.last_name
        title = document.title
        index = 0
        for revision in revDoc.revisions:
            body.append({
                "_id": str(revDoc.id),
                "date": revision.revDate,
                "title": title,
                "creator": name,
                'revType': revision.revType,
                'index': index,
                'email': collab.email
            })
            index += 1
    body = json.dumps(body)
    return ApiResult(
        body={'revision-history': json.loads(body)}
    )


@blueprint.route('/revision', methods=['GET'])
@fresh_jwt_required
def get_revision():
    """
    Retrieve a list of all the documents in the database.
    Returns
    -------
    Document[]
        List of collaborators currently in the system.
    """
    revisionIndex = request.form.get('index')
    revDocId = request.form.get('revDocId')
    revision = dao.get_document_rev(revDocId, revisionIndex)
    if revision is None:
        raise AdminServerApiError(
            msg='The revision document ID given was not found.',
            status=404
        )
    body = json.dumps(revision.to_json())
    return ApiResult(
        body={'revision': json.loads(body)}
    )
