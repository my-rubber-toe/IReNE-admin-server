"""
collaborators_dao.py
====================================
Data access object file for the collaborators.
"""

from daos.dummy_data.collaborator import collaborators

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
        Bans a collaborator found in the database.
        
        Parameters
        ----------
        collabID : string
            ID of the collaborator to be banned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the collaborator banned or None if the collaborator was not found.

        """
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = True
                return collab
        return None

    def unban_collaborator(self, collabID):
        """
        Unbans a collaborator found in the database.
        
        Parameters
        ----------
        collabID : string
            ID of the collaborator to be unbanned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the collaborator unbanned or None if the collaborator was not found.

        """
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = False
                return collab
        return None