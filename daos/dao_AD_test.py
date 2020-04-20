from mongoengine import *
from schema_DB import *
from dao_AD import *
import datetime
import init_db_test

"""
    DAO_AD_1 (Dao returns JSON object with admin)
"""
# adminID = Admin.objects()
# ids = []
# for x in adminID:
#     id_string = str(x.id)
#     ids.append(id_string)
# print(ids)
# admin_id = ids[0]
# print(get_login(admin_id))

"""
    DAO_AD_2 (Dao returns JSON with list of collabs not approved)
"""
# print(get_collab_request())

"""
    DAO_AD_3 (Dao approves collab request)
"""
# collabID = Collaborator.objects.filter(approved = False)
# ids = []
# for x in collabID:
#     id_string = str(x.id)
#     ids.append(id_string)
# print(ids)
# collab_ID = ids[0]
# current_status = Collaborator.objects.get(id= collab_ID)
# print("old status: ", current_status.email, current_status.approved)
# put_collab_request(collab_ID)
# new_status = Collaborator.objects.get(id= collab_ID)
# print("new status: ", new_status.email, new_status.approved)

"""
    DAO_AD_4 (DAO bans collaborator)
"""
# collabID = Collaborator.objects.filter(banned = False)
# ids = []
# for x in collabID:
#     id_string = str(x.id)
#     ids.append(id_string)
# collab_ID = ids[0]
# current_status = Collaborator.objects.get(id= collab_ID)
# print("old status: ", current_status.email, current_status.banned)
# banned_collab(collab_ID)
# new_status = Collaborator.objects.get(id= collab_ID)
# print("new status: ", new_status.email, new_status.banned)

"""
    DAO_AD_5 (DAO publish document)
"""
# docID = DocumentCase.objects.filter(published = False)
# ids = []
# for x in docID:
#     id_string = str(x.id)
#     ids.append(id_string)
# doc_ID = ids[0]
# current_status = DocumentCase.objects.get(id= doc_ID)
# print("old status: ", current_status.title, current_status.published)
# published_doc(doc_ID)
# new_status = DocumentCase.objects.get(id= doc_ID)
# print("new status: ", new_status.title, new_status.published)

"""
    DAO_AD_6 (DAO removes tag)
"""
tag_remove = 'Hurricane'
tags = Tag.objects
listtags = []
for x in tags:
    listtags.append(x.tagItem)
print("current tags", listtags)
docs = DocumentCase.objects()
print("current tags in list")
for x in docs:
    print(x.title, x.tagsDoc)
remove_tag(tag_remove)
newtags = Tag.objects
newlisttags = []
for x in newtags:
    newlisttags.append(x.tagItem)
print("new tags", newlisttags)
newdocs = DocumentCase.objects()
print("new tags in list")
for x in newdocs:
    print(x.title, x.tagsDoc)