from mongoengine import *
from schema_DB import *
import datetime
import json


def get_me(email_collab):
    get_collab = Collaborator.objects.get(email = email_collab)
    return json.loads(get_collab.to_json())

def get_doc_collab(collabid):
    get_docs = Document.objects.filter(creatoriD= collabid)
    return json.loads(get_docs.to_json())

def get_doc(docid):
    get_doc = DocumentCase.objects.get(id = docid)
    return json.loads(get_doc.to_json())

def remove_collab(collabid):
    Collaborator.objects(id = collabid).update_one(set__banned = True)

def remove_tag(tag):
    Tag.objects(tagItem = tag).delete()
    DocumentCase.objects().update(pull__tagsDoc= tag)

def get_tags_list():
    tag_objects = Tag.objects()
    return json.loads(tag_objects.to_json())

