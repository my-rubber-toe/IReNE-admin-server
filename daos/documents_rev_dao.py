"""
documents_dao.py
====================================
Data access object file for the admin accounts.
"""

from mongoengine import *
from database.schema_DB import DocumentCaseRevision, Revision
from datetime import datetime
import json


class RevDocumentsDAO:
    """
    Data access object for the Collaborators.
    """

    def __init__(self):
        pass

    def get_all_documents_rev(self):
        """
        Returns all the documents found in the database.
        
        Returns
        -------
        Dictionary[]
            List of documents found in the database.

        """      
        revDocs = DocumentCaseRevision.objects()
        return revDocs

    def get_document(self, documentID,):
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
            revDoc = DocumentCaseRevision.objects.get(id = documentID)
        except DoesNotExist:
            return None
        return revDoc

    def get_document_rev(self, documentID, revisionIndex):
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
            revDoc = DocumentCaseRevision.objects.get(id = documentID)
        except DoesNotExist:
            return None
        revision = revDoc.revisions[revisionIndex]
        return revision

    def update_rev_history(self, documentID, revType, **kwargs):
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
            revDoc = self.get_document(documentID)
            revision = Revision(**kwargs)
            revision.revType = revType
            revision.revDate = datetime.today().strftime('%Y-%m-%d')
            revDoc.revisions.append(revision)
            revDoc.save()
        except DoesNotExist:
            return None
        return revDoc
    
    def get_doc_revisions_by_type(self, documentID, revType):
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
            revisions = DocumentCaseRevision.objects.get(docId = documentID).revisions.filter(revType = revType)
        except DoesNotExist:
            return None
        return revisions