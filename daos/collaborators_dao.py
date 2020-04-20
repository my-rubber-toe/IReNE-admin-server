"""
collaborators_dao.py
====================================
Data access object file for the collaborators.
"""

from daos.dummy_data.collaborator import collaborators
from daos.dummy_data.document import documents

class CollaboratorsDAO:
    """
    Data access object for the Collaborators.
    """

    collaboratorList = []
    def __init__(self):
        for collab in collaborators:
            if(collab['approved'] == True):
                self.collaboratorList.append(collab)
    
    def get_collaborators(self):
        """
        Returns all the collaborators in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing collaborators.

        """
        return self.collaboratorList

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
        temp_collab = None
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = True
                temp_collab = collab
                break
        if(temp_collab is not None):
            for document in documents:
                if(document['_id'] in temp_collab['documentsID']):
                    document['published'] = False
        return temp_collab

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
        temp_collab = None
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = False
                temp_collab = collab
                break
        if(temp_collab is not None):
            for document in documents:
                if(document['_id'] in temp_collab['documentsID']):
                    document['published'] = True
        return temp_collab