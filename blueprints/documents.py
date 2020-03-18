from flask import Blueprint, Response, request

blueprint = Blueprint('documents', __name__, url_prefix='/admin/api/documents')

@blueprint.route('/', methods=['GET'])
def documents():
    """
    Retrieve a list of all the documents in the database.
    """
    return "Documents"

@blueprint.route('/view/<docID>', methods=['GET'])
def documents_view(docID):
    """
    Retrieve a list of metadata of all the documents in the database.
    """
    return "Document view ID: " + str(docID)

@blueprint.route('/publish', methods=['PUT'])
def documents_publish():
    """
    Set a document state to be pusblished.
    """
    return "Successful publish"

@blueprint.route('/unpublish', methods=['PUT'])
def documents_unpublish():
    """
    Set a document state to be unpublished.
    """
    return "Successful unpublish"
