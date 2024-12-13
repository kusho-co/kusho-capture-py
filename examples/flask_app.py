from flask import Flask, jsonify, request
import sys
import os

# Add parent directory to path to import sdk
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdk.collector import EventCollector
from sdk.middleware import WSGIMiddleware

app = Flask(__name__)

# Initialize the collector
collector = EventCollector(
    collector_url="http://localhost:7071",
    batch_size=1,  # Small batch size for testing
    flush_interval=5,  # Short interval for testing
    sample_rate=1.0  # Capture all requests for testing
)

# Add middleware
app.wsgi_app = WSGIMiddleware(
    app.wsgi_app,
    collector=collector
)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({
        'users': [
            {'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Jane'}
        ]
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({
        'message': 'User created',
        'user': data
    }), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({
        'id': user_id,
        'name': 'John Doe'
    })

@app.route('/not-captured')
def not_captured():
    return jsonify({
        'message': 'This endpoint should not be captured'
    })

if __name__ == '__main__':
    app.run(debug=True, port=3000)