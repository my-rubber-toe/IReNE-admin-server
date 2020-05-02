"""
collaborators_dao.py
====================================
Data access object file for the collaborators.
"""

from mongoengine import *
from database.schema_DB import Collaborator, DocumentCase
import datetime
import json

class CollaboratorsDAO:
    """
    Data access object for the Collaborators.
    """

    def __init__(self):
        pass
    
    def get_collaborators(self):
        """
        Returns all the collaborators in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing collaborators.

        """
        collabs = Collaborator.objects.filter(approved = True)
        return collabs

    def ban_collaborator(self, collabID):
        """
        Bans a collaborator found in the database and unpublishes all the documents pertaining to said collaborator.
        
        Parameters
        ----------
        collabID : string
            ID of the collaborator to be banned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the collaborator banned or None if the collaborator was not found.

        """
        try:
            collab = Collaborator.objects(id = collabID).update_one(set__banned = True)
            collaborator = Collaborator.objects.get(id = collabID)
            print(collaborator.documentsID)
            check = DocumentCase.objects(id__in = collaborator.documentsID).update(set__published = False, full_result = True)
            print(check.raw_result)
        except DoesNotExist:
            return None
        return collab

    def unban_collaborator(self, collabID):
        """
        Unbans a collaborator found in the database and publishes all the documents pertaining to said collaborator.
        
        Parameters
        ----------
        collabID : string
            ID of the collaborator to be unbanned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the collaborator unbanned or None if the collaborator was not found.

        """
        try:
            collab = Collaborator.objects(id = collabID).update_one(set__banned = False, full_result = True)
            collaborator = Collaborator.objects.get(id = collabID)
            DocumentCase.objects(id__in = collaborator.documentsID).update(set__published = True)
        except DoesNotExist:
            return None
        return collab

    def get_collab(self, collabID):
        """
        DAO that returns the collaborator of the id given

        Parameters
        ----------
        collabID : string
            ID of the collaborator to be returned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the collaborator or None if the collaborator was not found.
        """
        try:
            collab = Collaborator.objects.filter(id=collabID).first()
        except DoesNotExist:
            return None
        return collab
