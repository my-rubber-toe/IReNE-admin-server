from daos.dummy_data.access_request import requests

class AccessRequestsDAO:
    requestList = []
    def __init__(self):
        for collab in requests:
            if(collab['approved'] == False):
                self.requestList.append(collab)
    
    def get_access_requests(self):
        return self.requestList

    def accept_access_request(self, collabID):
        collab_temp = None
        for collab in self.requestList:
            if(collab.get('_id')==collabID and collab.get('approved') == False):
                collab['approved'] = True
                collab_temp = collab
        if(collab_temp is not None):
            self.requestList[:] = [collab for collab in self.requestList if collab.get('_id') != collabID ]
        return collab_temp

    def deny_access_request(self, collabID):
        collab_temp = None
        for collab in self.requestList:
            if(collab.get('_id')==collabID and collab.get('approved') == False):
                collab_temp = collab
        if(collab_temp is not None):
            self.requestList[:] = [collab for collab in self.requestList if collab.get('_id') != collabID ]
        return collab_temp