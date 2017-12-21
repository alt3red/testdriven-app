import os
from flask import Flask, jsonify


# instanciate the app
app = Flask(__name__)

# set config
app.settings = os.getenv('APP_SETTINGS')
app.config.from_object(app.settings)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
})
