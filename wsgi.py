#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

from api import create_app
app = application = create_app('flask_config.ProductionConfig')
application.secret_key = 'Add your secret key'
