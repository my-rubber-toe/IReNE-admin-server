"""
documents_rev_dao.py
====================================
Data access object file for the revision history.
"""

from mongoengine import *
from database.schema_DB import document_case_revision
from mongoengine.queryset.visitor import Q
from datetime import datetime
import json


class RevDocumentsDAO:
    """
    Data access object for the Revision History.
    """

    def __init__(self):
        pass

    def get_documents_revisions(self, sortField, sortOrder, filterVal, pageNumber, pageSize):
        """
        Gets all the revisions found in the system with the given specifications.
        
        Parameters
        ----------
        sortField : string
            Field to be used to sort the output
        sortOrder : string
            Asc or Desc, sort order of the output
        filterVal : string
            Value to be used to filter the revisions
        pageNumber :  number
            Number of pages that the user wants in return
        pageSize : number
            Number of revisions per page that the user wants in return
        
        Returns
        -------
        List
            List of the objects that follow the given parameters

        """
        sortParam = sortField
        try:
            filterValInt = int(filterVal)
        except:
            filterValInt = None
        if(sortOrder == 'desc'):
            sortParam = "-" + sortField
        objects = document_case_revision.objects(Q(revision_date__icontains = filterVal) |
                                    Q(revision_number = filterValInt) |
                                    Q(document_title__icontains = filterVal) |
                                    Q(creator_name__icontains = filterVal) |
                                    Q(revision_type__icontains = filterVal)
                                    ).order_by(sortParam)
        length = objects.count()
        return objects[pageNumber*pageSize:(pageNumber*pageSize)+pageSize], length
        
    def get_document_rev(self, documentID):
        """
        Gets the document revision with the given ID from the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document revision to be returned.
        
        Returns
        -------
        DocumentCaseRevision
            Returns a DocumentCaseRevision object or None if the document was not found.

        """
        try:
            revDoc = document_case_revision.objects.get(id = documentID)
        except DoesNotExist:
            return None
        return revDoc