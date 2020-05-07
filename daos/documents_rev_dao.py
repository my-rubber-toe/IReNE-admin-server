"""
documents_dao.py
====================================
Data access object file for the admin accounts.
"""

from mongoengine import *
from database.schema_DB import DocumentCaseRevision
from mongoengine.queryset.visitor import Q
from datetime import datetime
import json


class RevDocumentsDAO:
    """
    Data access object for the Collaborators.
    """

    def __init__(self):
        pass

    def get_documents_revisions(self, sortField, sortOrder, filterVal, pageNumber, pageSize):
        sortParam = sortField
        if(sortOrder == 'desc'):
            sortParam = "-" + sortField
        objects = DocumentCaseRevision.objects(Q(revision_date__icontains = filterVal) |
                                    Q(revision_number__icontains = filterVal) |
                                    Q(document_title__icontains = filterVal) |
                                    Q(creator_name__icontains = filterVal) |
                                    Q(revision_type__icontains = filterVal)
                                    ).order_by(sortParam)
        length = objects.count()
        return objects[pageNumber*pageSize:(pageNumber*pageSize)+pageSize], length
        
    def get_document_rev(self, documentID):
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