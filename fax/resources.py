from flask import Flask, request
from flask_restful import Resource, Api, abort
import json
from local_phaxio.utils import (
    make_faxio_request,
    build_faxio_request,
)
from werkzeug.exceptions import (
    BadRequest,
)


def decode_response_json(response_json: str) -> dict:
    return json.loads(response_json.decode('utf-8'))


class FaxResource(Resource):
    def post(self):
        try:
            my_data = decode_response_json(request.data)
            phaxio_request_body = build_faxio_request(my_data)
            response_data = make_faxio_request(phaxio_request_body)
            if not response_data.get('success', None):
                abort(400, status="Failed", message="Issue with fax")
            client_response = {
                "status": "Success!",
                "fax_id": response_data['faxId']
            }
            return client_response
        except BadRequest:
            raise
        except Exception as e:
            abort(400, message=e.args[0], status="Failed")
