"""
admin_dao.py
====================================
Data access object file for the admin accounts.
"""
from flask_bcrypt import Bcrypt
from mongoengine import *
from database.schema_DB import Admin
import datetime
import json

bcrypt = Bcrypt()
class AdminDAO:
    """
    Data access object for the Admin accounts.
    """

    def __init__(self):
        pass
    
    def get_admin(self, username):
        """
        Returns the admin account with the given username. 
        
        Parameters
        ----------
        username : string
            Username of the admin account to be found.
        
        Returns
        -------
        Dictionary
            Dictionary of the admin account and its values in the database or None if no account was found.

        """
        try:
            admin = Admin.objects.get(username = username)
        except DoesNotExist:
            return None
        return admin
    
    def check_password(self, password_hash, password):
        """
        Checks if the password given matches the password hashed.
        
        Parameters
        ----------
        password_hash : string
            Password hash to compare.
        password : string
            Password to be tested.
        
        Returns
        -------
        bool
            True if the password matches, false otherwise.

        """
        return bcrypt.check_password_hash(password_hash, password)