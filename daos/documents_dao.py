"""
documents_dao.py
====================================
Data access object file for the admin accounts.
"""

from mongoengine import *
from database.schema_DB import DocumentCase, Collaborator
import datetime
import json
from bson.json_util import dumps


class DocumentsDAO:
    """
    Data access object for the Collaborators.
    """

    def __init__(self):
        pass

    def get_all_documents(self):
        """
        Returns all the documents found in the database.
        
        Returns
        -------
        Dictionary[]
            List of documents found in the database.

        """

        docs = DocumentCase.objects.aggregate(*[
            {
                '$lookup': {
                    'from': Collaborator._get_collection_name(),
                    'localField': 'creatoriD',
                    'foreignField': '_id',
                    'as': 'creator'
                }
            },
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'title': True,
                    'published': True,
                    'creator': {
                        '$let': {
                            'vars': {
                                'tmp': {'$arrayElemAt': ["$creator", 0]}
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
        Dictionary
            Returns a dictionary as the document or None if the document was not found.

        """
        try:
            doc = DocumentCase.objects.get(id=documentID)
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
        Dictionary
            Returns a dictionary as the document published or None if the document was not found.

        """
        try:
            doc = DocumentCase.objects(id=documentID).update_one(set__published=True)
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
        Dictionary
            Returns a dictionary as the document unpublished or None if the document was not found.

        """
        try:
            doc = DocumentCase.objects(id=documentID).update_one(set__published=False)
        except DoesNotExist:
            return None
        return doc
