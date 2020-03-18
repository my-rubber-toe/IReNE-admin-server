from flask import Response, json
from werkzeug.datastructures import Headers
"""
Classes to standardize the response methods.
Improves the ease of debugging
"""


class ApiException(object):
    """API exception response wrapper class"""

    def __init__(self,  message, error_type='Error', status=400):
        self.status = status
        self.error_type = error_type
        self.message = message

    def to_result(self):
        return Response(
            json.dumps(
                {
                    'error': {
                        'status': self.status,
                        'type': self.error_type,
                        'message': self.message,
                        
                    }
                }
            ),
            headers=add_headers(),
            status=self.status,
            mimetype='application/json'
        )


class ApiResult(object):
    """API result response wrapper class"""

    def __init__(self, message, status=200):
        self.message = message
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.message),
                        headers=add_headers(),
                        status=self.status,
                        mimetype='application/json')



def add_headers():
    h = Headers()
    # add headers here
    return h

