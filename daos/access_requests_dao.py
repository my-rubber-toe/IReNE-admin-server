"""
access_requests_dao.py
====================================
Data access object file for the access requests item. Important; Access Request objects are in truth Collaborators object in the databse whose 'approved' flag is false.
"""

from mongoengine import *
from database.schema_DB import collaborator
import datetime
import json

class AccessRequestsDAO:
    """
    Data access object for the Access Requests.
    """
    def __init__(self):
        pass
    
    def get_access_requests(self):
        """
        Returns all the access requests in the database. 
        
        Returns
        -------
        Collaborator[]
            List of collaborators representing the Access Requests in the database.

        """
        access_req = collaborator.objects.filter(approved = False)
        return access_req

    def accept_access_request(self, arID):
        """
        Accepts an access request found in the database.
        
        Parameters
        ----------
        arID : string
            ID of the access request to be accepted.
        
        Returns
        -------
        Collaborator
            Collaborator object of the item that matched the ID or None if the collaborator was not found.

        """
        collab = collaborator.objects(id = arID).update_one(set__approved = True)
        if(collab == 0):
            return None
        return collab

    def deny_access_request(self, arID):
        """
        Denies an access request found in the database by removing it.
        
        Parameters
        ----------
        arID : string
            ID of the access request to be denied.
        
        Returns
        -------
        Collaborator
            Collaborator object of the item that matched the ID or None if the collaborator was not found.


        """
        collab = collaborator.objects(id = arID).delete()
        if(collab == 0):
            return None
        return collab