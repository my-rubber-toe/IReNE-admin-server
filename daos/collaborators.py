from daos.dummy_data.collaborator import requests

class CollaboratorsDAO:
    collaboratorList = []
    def __init__(self):
        for collab in requests:
            if(collab['approved'] == True):
                self.collaboratorList.append(collab)
    
    def get_collaborators(self):
        return self.collaboratorList

    def ban_collaborator(self, collabID):
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = True
                return collab
        return None

    def unban_collaborator(self, collabID):
        for collab in self.collaboratorList:
            if(collab.get('_id')==collabID and collab.get('approved') == True):
                collab['banned'] = False
                return collab
        return None