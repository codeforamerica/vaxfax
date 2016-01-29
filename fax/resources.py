from flask import Flask, request
from flask_restful import Resource, Api
import json
from local_phaxio.utils import (
    make_faxio_request,
    build_faxio_request,
)


class FaxResource(Resource):
    def post(self):
        # import pdb; pdb.set_trace()
        # my_data = request.form['data']
        my_data = json.loads(request.data.decode('utf-8'))
        return my_data
