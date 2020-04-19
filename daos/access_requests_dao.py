"""
access_requests_dao.py
====================================
Data access object file for the access requests item. Important; Access Request objects are in truth Collaborators object in the databse whose 'approved' flag is false.
"""
from daos.dummy_data.access_request import requests

class AccessRequestsDAO:
    """
    Data access object for the Access Requests.
    """
    requestList = []
    def __init__(self):
        for ar in requests:
            if(ar['approved'] == False):
                self.requestList.append(ar)
    
    def get_access_requests(self):
        """
        Returns all the access requests in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing the Access Requests in the database.

        """
        return self.requestList

    def accept_access_request(self, arID):
        """
        Accepts an access request found in the database.
        
        Parameters
        ----------
        arID : string
            ID of the access request to be accepted.
        
        Returns
        -------
        Dictionary
            Returns a dictionary of the access request accepted or None if the access request was not found.

        """
        ar_temp = None
        for ar in self.requestList:
            if(ar.get('_id')==arID and ar.get('approved') == False):
                ar['approved'] = True
                ar_temp = ar
        if(ar_temp is not None):
            self.requestList[:] = [ar for ar in self.requestList if ar.get('_id') != arID ]
        return ar_temp

    def deny_access_request(self, arID):
        """
        Denies an access request found in the database.
        
        Parameters
        ----------
        arID : string
            ID of the access request to be denied.
        
        Returns
        -------
        Dictionary
            Returns a dictionary of the access request denied or None if the access request was not found.

        """
        ar_temp = None
        for ar in self.requestList:
            if(ar.get('_id')==arID and ar.get('approved') == False):
                ar_temp = ar
        if(ar_temp is not None):
            self.requestList[:] = [ar for ar in self.requestList if ar.get('_id') != arID ]
        return ar_temp