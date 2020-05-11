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
    The username is valid if it is between 6 and 20 characters, contains only alphanumeric characters and doesn't start
    end or consecutively repeat dots.
    
    Parameters
    ----------
        username : string
            username to be evaluated.
    
    Returns
    -------
    bool
        True if valid, false otherwise.

    """
    match = re.search(r'(^[a-zA-Z](?!\.)(?!.*\.$)(?!.*?\.\.)[a-zA-Z0-9_.]{5,19})$',username)
    if(match is None):
        return False
    else:
        return True

def password_isvalid(password):
    """
    Returns whether or not the password given is in a valid format.
    The password is valid if its length is greater or equal to 8, and contains at least one upper case letter, one lower case letter and a number.
    
    Parameters
    ----------
        password : string
            password to be evaluated.
    
    Returns
    -------
    bool
        True if valid, false otherwise.

    """
    match = re.search(r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d\w].{8,}', password)
    if(match is None):
        return False
    else:
        return True