"""
documents_rev.py
Every route regarding documents revision, including getting all the revision history of the different documents found in the system and filter and sort those revisions.
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
    """
    Retrieve a list of revision history based on the parameters given.

    Returns
    -------
    DocumentCaseRevision[]
        List of DocumentCaseRevision that matched the given specifications.
    """
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
    Retrieve a DocumentCaseRevision to be viewd.

    Returns
    -------
    DocumentCaseRevision[]
        DocumentCaseRevision that matched the given Id.

    ApiException
        Exception if the revision ID given was not fount.
    
    """
    revDocId = request.form.get('revDocId')
    valid_revdoc_id = objectId_is_valid(revDocId)
    if not valid_revdoc_id:
        return ApiException(
            error_type = "Validation Error",
            message='The revision document ID given is not valid.',
            status=400
        )
    revision = dao.get_document_rev(revDocId)
    if revision is None:
        return ApiException(
            error_type="Database Error",
            message='The revision document ID given was not found.',
            status=404
        )
    
    body = {'new': revision.field_changed.new.to_json(),
            'old': revision.field_changed.old.to_json()}
    return ApiResult(
        body={'revision': body}
    )