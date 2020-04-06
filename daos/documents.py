from daos.dummy_data.document import documents

class DocumentsDAO:
    documentList = []

    def __init__(self):
        self.documentList = documents

    def get_all_documents(self):
        return self.documentList

    def get_document(self, documentID):
        for document in self.documentList:
            if (document['_id']==documentID):
                return document
        return None

    def publish_document(self, documentID):
        for document in self.documentList:
            if(document.get('_id')==documentID):
                document['published'] = True
                return document
        return None
    
    def unpublish_document(self, documentID):
        for document in self.documentList:
            if(document.get('_id')==documentID):
                document['published'] = False
                return document
        return None