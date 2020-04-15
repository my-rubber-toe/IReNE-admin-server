from flask import make_response, jsonify
import json
from flask import Response

"""
Classes to standardize the response methods.
Improves the ease of debugging
"""


class ApiException(object):
    """API exception response wrapper class"""
    def __init__(self, error_type='ApiError', message='Error', status=500, content_type = 'application/json'):
        self.res = json.dumps({"error_type":error_type, "message":message, 'status': status})
        self.status = status
        self.content_type = content_type

    def to_result(self):
        return make_response(Response(self.res, headers={'Content-Type': self.content_type}), self.status)

class ApiResult(object):
    """API result response wrapper class"""

    def __init__(self, body, status=200, content_type='application/json'):
        self.body = json.dumps(body)
        self.status = status
        self.content_type = content_type

    def to_response(self):
        return make_response(Response(self.body, headers={'Content-Type': self.content_type}), self.status)
