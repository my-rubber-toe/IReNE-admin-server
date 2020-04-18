"""
tags_dao.py
====================================
Data access object file for the admin accounts.
"""

from daos.dummy_data.tag import tags

class TagsDAO:
    """
    Data access object for the Admin accounts.
    """
    tagList = []
    
    def __init__(self):
        self.tagList = tags

    def get_tags(self):
        """
        Returns all the tags found in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing the tags in the database.

        """
        return self.tagList
    
    def remove_tag(self, tagID):
        """
        Removes a Tag from the database.
        
        Parameters
        ----------
        tagID : string
            Id of the tag to be removed.
        
        Returns
        -------
        Dictionary
            Dictionary of the tag removed None if no tag was found.

        """
        tag_temp = None
        for tag in self.tagList:
            if(tag.get('_id')==tagID):             
                tag_temp =  tag
        if(tag_temp is not None):
            self.tagList[:] = [tag for tag in self.tagList if tag.get('_id') != tagID ]
        return tag_temp