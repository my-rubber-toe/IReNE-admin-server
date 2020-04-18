"""
admin_dao.py
====================================
Data access object file for the admin accounts.
"""
from daos.dummy_data.admin import admins
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
class AdminDAO:
    """
    Data access object for the Admin accounts.
    """
    adminList = []

    def __init__(self):
        self.adminList = admins
    
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
        for admin in self.adminList:
            if (admin.get('username') == username):
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