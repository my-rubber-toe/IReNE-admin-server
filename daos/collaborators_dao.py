"""
collaborators_dao.py
====================================
Data access object file for the collaborators.
"""

from mongoengine import *
from database.schema_DB import collaborator, document_case
from bson.json_util import dumps
from utils.email_manager import EmailManager


class CollaboratorsDAO:
    """
    Data access object for the Collaborators.
    """

    def __init__(self):
        self.email_manager = EmailManager()

    def get_collaborators(self):
        """
        Returns all the collaborators in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing collaborators.

        """
        collabs = collaborator.objects.filter(approved=True).aggregate(*[
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
        Collaborator
            Collaborator object of the item that matched the ID or None if the collaborator was not found.

        """
        try:
            collaborator.objects(id=collabID).update_one(set__banned=True, full_result=True)
            collab = collaborator.objects.get(id=collabID)
        except DoesNotExist:
            return None
        try:
            document_case.objects(creatoriD=collab.id).update(set__published=False, full_result=True)
        except:
            pass
        self.email_manager.email_collaborator(email=collab.email, email_type='ban')
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
        Collaborator
            Collaborator object of the item that matched the ID or None if the collaborator was not found.
        """
        try:
            collaborator.objects(id=collabID).update_one(set__banned=False, full_result=True)
            collab = collaborator.objects.get(id=collabID)
        except DoesNotExist:
            return None
        try:
            document_case.objects(creatoriD=collab.id).update(set__published=True, full_result=True)
            self.email_manager.email_collaborator(email=collab.email, email_type='unban')
        except:
            pass
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
        Collaborator
            Collaborator object of the item that matched the ID or None if the collaborator was not found.
        """
        try:
            collab = collaborator.objects.filter(id=collabID).first()
        except DoesNotExist:
            return None
        return collab
