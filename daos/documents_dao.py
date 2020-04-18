"""
documents_dao.py
====================================
Data access object file for the admin accounts.
"""

from daos.dummy_data.document import documents

class DocumentsDAO:
    """
    Data access object for the Collaborators.
    """
    documentList = []

    def __init__(self):
        self.documentList = documents

    def get_all_documents(self):
        """
        Returns all the documents found in the database.
        
        Returns
        -------
        Dictionary[]
            List of documents found in the database.

        """      
        return self.documentList

    def get_document(self, documentID):
        """
        Gets the document with the given ID from the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document to be returned.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the document or None if the document was not found.

        """
        for document in self.documentList:
            if (document['_id']==documentID):
                return document
        return None

    def publish_document(self, documentID):
        """
        Publishes the document with the given ID in the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document to be published.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the document published or None if the document was not found.

        """
        for document in self.documentList:
            if(document.get('_id')==documentID):
                document['published'] = True
                return document
        return None
    
    def unpublish_document(self, documentID):
        """
        Unpublished the document with the given ID in the database.
        
        Parameters
        ----------
        documentID : string
            ID of the document to be unpublished.
        
        Returns
        -------
        Dictionary
            Returns a dictionary as the document unpublished or None if the document was not found.

        """
        for document in self.documentList:
            if(document.get('_id')==documentID):
                document['published'] = False
                return document
        return None