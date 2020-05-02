"""
collaborators_dao.py
====================================
Data access object file for the collaborators.
"""

from mongoengine import *
from database.schema_DB import Collaborator, DocumentCase
from bson.json_util import dumps


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
        collabs = Collaborator.objects.filter(approved=True).aggregate(*[
            {
                '$project': {
                    '_id': {'$toString': '$_id'},
                    'first_name': True,
                    'last_name': True,
                    'email': True,
                    'banned': True
                }
            }
        ])
        return dumps(collabs)

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
            collab = Collaborator.objects(id=collabID).update_one(set__banned=True)
            collaborator = Collaborator.objects.get(id=collabID)
            DocumentCase.objects(creatoriD=collaborator.id).update(set__published=False, full_result=True)
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
            collab = Collaborator.objects(id=collabID).update_one(set__banned=False, full_result=True)
            collaborator = Collaborator.objects.get(id=collabID)
            DocumentCase.objects(creatoriD=collaborator.id).update(set__published=True, full_result=True)
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
