import os
from flask import Flask


""" Flask blueprint """
app = Flask(__name__)


""" IF DEBUG """
if __name__ == "__main__":
    debug = True if os.environ.get('PYTHON_ENV') != 'production' else False
    app.run(host="0.0.0.0", debug=debug, use_reloader=False, threaded=True)
