from flask import Flask, request
from gcp.cloud_functions import handle_group_me_message

if __name__ == "__main__":
    app = Flask(__name__)


    @app.route('/', methods=["POST"])
    def index():
        return handle_group_me_message(request)


    app.run('127.0.0.1', 8000)
