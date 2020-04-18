"""
validators.py
====================================
Methods that are used to validate any input from the user.
"""
from bson import ObjectId
import re

def objectId_is_valid(object_id):
    """
    Returns whether or not the object id given is a valid MongoDB ObjectId.

    Parameters
    ----------
        object_id : string
            ID of the object to be evaluated.
    
    Returns
    -------
    bool
        True if valid, false otherwise.

    """
    return ObjectId.is_valid(object_id)

def username_isvalid(username):
    """
    Returns whether or not the username given is valid.
    
    Parameters
    ----------
        username : string
            username to be evaluated.
    
    Returns
    -------
    bool
        True if valid, false otherwise.

    """
    match = re.search(r'^(?![.])(?!.*[.]{2})[\w.]{6,20}(?<![.])$',username)
    if(match is None):
        return False
    else:
        return True

def password_isvalid(password):
    """
    Returns whether or not the password given is in a valid format.
    
    Parameters
    ----------
        password : string
            password to be evaluated.
    
    Returns
    -------
    bool
        True if valid, false otherwise.

    """
    match = re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,30}$", password)
    if(match is None):
        return False
    else:
        return True