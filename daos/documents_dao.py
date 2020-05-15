"""
documents_dao.py
====================================
Data access object file for the documents in the system.
"""

from mongoengine import *
from database.schema_DB import document_case, collaborator
from bson.json_util import dumps
from utils.email_manager import EmailManager


class DocumentsDAO:
    """
    Data access object for the Documents.
    """

    def __init__(self):
        self.email_manager = EmailManager()

    def get_all_documents(self):
        """
        Returns all the documents found in the database.
        
        Returns
        -------
        Dictionary[]
            List of documents found in the database.

        """
        # Object list cotains: _id, title, published, creator
        docs = document_case.objects.aggregate(*[
            {
                '$lookup': {
                    'from': collaborator._get_collection_name(),
                    'localField': 'creatoriD',
                    'foreignField': '_id',
                    'as': 'creatorName'
                }
            },
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'title': 1,
                    'published': 1,
                    'creator': {
                        '$let': {
                            'vars': {
                                'tmp': {'$arrayElemAt': ["$creatorName", 0]}
                            },
                            'in': {
                                '$concat': ['$$tmp.first_name', ' ', '$$tmp.last_name']
                            }
                        }
                    }
                }
            }
        ])
        return dumps(docs)

    def get_document(self, documentID):
        """
        Gets the document with the given ID from the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document to be returned.
        
        Returns
        -------
        DocumentCase
            DocumentCase object of the item that matched the ID or None if the document was not found.

        """
        try:
            doc = document_case.objects.get(id=documentID)
        except DoesNotExist:
            return None
        return doc

    def publish_document(self, documentID):
        """
        Publishes the document with the given ID in the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document to be published.
        
        Returns
        -------
        DocumentCase
            DocumentCase object of the item that matched the ID or None if the document was not found.

        """
        try:
            document_case.objects(id=documentID).update_one(set__published=True, full_result=True)
            doc: document_case = document_case.objects.get(id=documentID)

            # Automatically fetches collaborator since its a reference field
            collab: collaborator = doc.creatoriD

            self.email_manager.email_collaborator(doc_title=doc.title, email=collab.email, email_type='publish')
        except DoesNotExist:
            return None

        return doc

    def unpublish_document(self, documentID):
        """
        Unpublished the document with the given ID in the database.

        Parameters
        ----------
        documentID : string
            ID of the document to be unpublished.

        Returns
        -------
        DocumentCase
            DocumentCase object of the item that matched the ID or None if the document was not found.

        """
        try:
            document_case.objects(id=documentID).update_one(set__published=False, full_result=True)
            doc: document_case = document_case.objects.get(id=documentID)
            # Automatically fetches collaborator since its a reference field
            collab: collaborator = doc.creatoriD

            self.email_manager.email_collaborator(doc_title=doc.title, email=collab.email, email_type='unpublish')
        except DoesNotExist:
            return None

        return doc
