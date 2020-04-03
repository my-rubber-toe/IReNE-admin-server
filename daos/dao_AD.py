from mongoengine import *
from schema_DB import *
import datetime
import json

def get_login(adminID):
    get_admins = Admin.objects.get(id = adminID)
    return json.loads(get_admins.to_json())

def get_collab_request():
    get_collab_req = Collaborator.objects.filter(approved = False)
    return json.loads(get_collab_req.to_json())

def put_collab_request(collabid):
    Collaborator.objects(id = collabid).update_one(set__approved = True)

def get_collabs():
    get_collabs = Collaborator.objects.filter(approved = True)
    return json.loads(get_collabs.to_json())

def remove_collab(collabid):
    Collaborator.objects(id = collabid).delete()

def banned_collab(collabid):
    Collaborator.objects(id = collabid).update_one(set__banned = True)

def unbanned_collab(collabid):
    Collaborator.objects(id = collabid).update_one(set__banned = False)

def get_doc_collab(collabid):
    get_docs = Document.objects.filter(creatoriD= collabid)
    return json.loads(get_docs.to_json())

def get_doc(docid):
    get_doc = DocumentCase.objects.get(id = docid)
    return json.loads(get_doc.to_json())

def get_docs():
    get_doc = DocumentCase.objects()
    return json.loads(get_doc.to_json())

def published_doc(docid):
    DocumentCase.objects(id = docid).update_one(set__published = True)

def unpublished_doc(docid):
    DocumentCase.objects(id = docid).update_one(set__published = False)

def remove_tag(tag):
    Tag.objects(tagItem = tag).delete()
    DocumentCase.objects().update(pull__tagsDoc= tag)

def get_tags_list():
    tag_objects = Tag.objects()
    return json.loads(tag_objects.to_json())
