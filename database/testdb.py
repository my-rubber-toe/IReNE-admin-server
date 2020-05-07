from mongoengine import *
from mock_data_revisions import *
from schema_DB import DocumentCase, Collaborator
import datetime

disconnect()
# import regex
#Connection to the Database
connect('IReNEdb')
#connec the db for testing purposes
#connect('IReNEdb', host='mongomock://localhost:27017')

class Revision(EmbeddedDocument):
    revDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    revType = StringField(required=True)
    fields = DictField(required=True)

class DocumentCaseRevision(Document):
    creatorId = StringField(min_length=1, required=True)
    docId =  StringField(min_length=1, required=True)
    revisions = ListField(EmbeddedDocumentField(Revision))

class DocumentCaseRevision(Document):
    creatorId = StringField(min_length=1, required=True)
    docId =  StringField(min_length=1, required=True)
    creator_name =StringField(min_length=1, required=True)
    creator_email =StringField(min_length=1, required=True)
    document_title =  StringField(min_length=1, required=True)
    revision_date = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    revision_type = StringField(required=True)
    fields_changed = DictField(required=True)

collab5 = Collaborator(first_name="Yomar", last_name="Ruiz", email="yomar.ruiz@upr.edu")
collab5.save()
collab3 = Collaborator(first_name="Alberto", last_name="Canela", email="alberto.canela@upr.edu")
collab3.save()

# creation[0]['creatoriD'] = str(collab5.id)
# creation[1]['creatoriD'] = str(collab3.id)
# document1 = DocumentCase(**creation[0])
# document1.save()
# document2 = DocumentCase(**creation[1])
# document2.save()
# fakeHist[0]['creatorId'] = str(collab5.id)
# fakeHist[1]['creatorId'] = str(collab3.id)
# fakeHist[2]['creatorId'] = str(collab5.id)

# fakeHist[0]['docId'] = str(document1.id)
# fakeHist[1]['docId'] = str(document2.id)
# fakeHist[2]['docId'] = str(document1.id)

# for i in range(0,166):
#     doc = DocumentCaseRevision(**fakeHist2[1])
#     doc.save()

for i in fakeHist:
    doc = DocumentCaseRevision2(**fakeHist2[0])
    doc.save()