'''Top level api folder, for holding the api library
'''


from flask import Flask
from flask.ext.restful import (
    Api,
)
from fax.resources import (
    FaxResource,
)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    api = Api(app)

    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
      return response

      
    api.add_resource(FaxResource, '/fax')
    api.init_app(app)

    return app



    #
    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)
    #
    # return app
