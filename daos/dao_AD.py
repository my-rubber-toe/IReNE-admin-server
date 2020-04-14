from mongoengine import *
from schema_DB import *
import datetime
import json

def get_login(adminID):
    """
        DAO that returns admin info in JSON
    """
    get_admins = Admin.objects.get(id = adminID)
    return json.loads(get_admins.to_json())

def get_collab_request():
    """
        DAO that returns list of collabs that hasn't been approved yet
    """
    get_collab_req = Collaborator.objects.filter(approved = False)
    return json.loads(get_collab_req.to_json())

def put_collab_request(collabid):
    """
        DAO that approved an collab request
    """
    Collaborator.objects(id = collabid).update_one(set__approved = True)


def get_collabs():
    """
        DAO that returns list of collabs that were approved approved
    """
    get_collabs = Collaborator.objects.filter(approved = True)
    return json.loads(get_collabs.to_json())

def remove_collab(collabid):
    """
        DAO that deletes a collaborator
    """
    Collaborator.objects(id = collabid).delete()

def banned_collab(collabid):
    """
        DAO that ban a collaborator
    """
    Collaborator.objects(id = collabid).update_one(set__banned = True)

def unbanned_collab(collabid):
    """
        DAO that unban a collaborator
    """
    Collaborator.objects(id = collabid).update_one(set__banned = False)

def get_doc_collab(collabid):
    """
        DAO that returns list of documents by a collab
    """
    get_docs = Document.objects.filter(creatoriD= collabid)
    return json.loads(get_docs.to_json())

def get_doc(docid):
    """
        DAO that returns a specific document
    """
    get_doc = DocumentCase.objects.get(id = docid)
    return json.loads(get_doc.to_json())

def get_docs():
    """
        DAO that returns list of documents
    """
    get_doc = DocumentCase.objects()
    return json.loads(get_doc.to_json())

def published_doc(docid):
    """
        DAO that publishes a document
    """
    DocumentCase.objects(id = docid).update_one(set__published = True)

def unpublished_doc(docid):
    """
        DAO that unpublishes a document
    """
    DocumentCase.objects(id = docid).update_one(set__published = False)

def remove_tag(tag):
    """
        DAO that removes a tag
    """
    Tag.objects(tagItem = tag).delete()
    DocumentCase.objects().update(pull__tagsDoc= tag)

def get_tags_list():
    """
        DAO that returns list of tags
    """
    tag_objects = Tag.objects()
    return json.loads(tag_objects.to_json())
