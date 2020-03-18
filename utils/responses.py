from flask import Response, json
from werkzeug.datastructures import Headers
"""
Classes to standardize the response methods.
Improves the ease of debugging
"""


class ApiException(object):
    """API exception response wrapper class"""

    def __init__(self,  message, _type='Error', status=400):
        self.message = message
        self.status = status
        self._type = _type

    def to_result(self):
        return Response(
            json.dumps(
                {
                    'error': {
                        'type': self._type,
                        'message': self.message,
                        'status': self.status
                    }
                }
            ),
            headers=add_headers(),
            status=self.status,
            mimetype='application/json'
        )


class ApiResult(object):
    """API result response wrapper class"""

    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value),
                        headers=add_headers(),
                        status=self.status,
                        mimetype='application/json')



def add_headers():
    h = Headers()
    # add headers here
    return h

