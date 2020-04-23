"""
tags_dao.py
====================================
Data access object file for the admin accounts.
"""

from mongoengine import *
from database.schema_DB import Tag, DocumentCase
import datetime
import json


class TagsDAO:
    """
    Data access object for the Admin accounts.
    """
    
    def __init__(self):
        pass

    def get_tags(self):
        """
        Returns all the tags found in the database. 
        
        Returns
        -------
        Dictionary[]
            List of dictionaries representing the tags in the database.

        """
        tag_objects = Tag.objects()
        return json.loads(tag_objects.to_json())
    
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
        try:
            Tag.objects(tagItem = tagID).delete()
            DocumentCase.objects().update(pull__tagsDoc= tag)
            return tagID
        except DoesNotExist:
            return None