from flask import Flask, request
from flask_restful import Resource, Api
import json

class FaxResource(Resource):
    def post(self):
        # import pdb; pdb.set_trace()
        # my_data = request.form['data']
        my_data = json.loads(request.data.decode('utf-8'))
        return my_data
