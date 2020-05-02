"""
handler.py
====================================
Data access object file for the access requests item. Important; Access Request objects are in truth Collaborators object in the databse whose 'approved' flag is false.
"""

import datetime

class AdminServerError(Exception):
    """
    Handler for all the errors that occur during the execution of the server.
    """
    error_type = 'AdminServerError'

    def __init__(self, err=None, msg='Error', status=500, user='', action=None):
        self.msg = msg
        self.status = status
        if err:
            self.error_stack = [str(x).replace('"', "'") for x in err.args]
        else:
            self.error_stack = []
        self.error_stack.append(msg)
        self.err = err
        self.user = user
        self.action = action
        self.status = status
        self.now = datetime.datetime.now()
        self.log()

    def log(self):
        """
        Logs the error that just occured into the database.

        """
        log_string = '"error":"{}","error_type":"{}","user":"{}","log_action":"{}",' \
                     '"error_description":"{}","status":"{}", "time_stamp": "{}"'.format(
            str(self.err).replace('"', "'"),
            str(self.error_type).replace('"', "'"),
            str(self.user),
            str(self.action).replace('"', "'"),
            str(self.error_stack),
            str(self.status),
            str(self.now.strftime("%a, %d %b %Y %I:%M:%S %p"))
        )
        log_string = '{' + log_string + '},\n'

        # TODO: implement buffer
        with open('error_logs.log', 'a+') as f:
            f.write(log_string)

    def __str__(self):
        """
        Turns the error object into a string.
        
        Returns
        -------
        string
            String representing the error object.
        """
        return {'error': self.error_type, 'message':self.msg, 'status':self.status}

class AdminServerApiError(AdminServerError):
    """
    Handler for all the errors that occur during the execution of the server.

    ...

    Methods
    -------
    __init__(err=None, msg='Error', status=500, user='', action=None)
       Base contructor of the class. Initializes instance variables.
    log()
        Logs the error that just ocurred in a log file.
    __str__()
        Returns string representation of the error.
    """
    error_type = "AdminServerApiError"

class AdminServerAuthError(AdminServerError):
    """
    Class representing the error type.

    """
    error_type = "AdminServerAuthError"

class AdminServerRequestError(AdminServerError):
    """
    Class representing the error type.

    """
    error_type = "AdminServerRequestError"