from flask import Flask, request, jsonify, abort
from flask_restful import Api , Resource

app = Flask(__name__)

# In-memory storage for users: {user_id: { "name": ..., "email": ... }}
users = {}
next_id = 1  # For generating simple incremental user IDs

@app.route('/users', methods=['GET'])
def list_users():
    """Return the full list of users."""
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return a single user's data by ID."""
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found.")
    return jsonify({user_id: user})

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user with name and email in JSON payload."""
    global next_id
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Payload must include 'name' and 'email'.")
    user_id = next_id
    users[user_id] = {"name": data['name'], "email": data['email']}
    next_id += 1
    return jsonify({"id": user_id, **users[user_id]}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user's data by ID."""
    data = request.get_json()
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found.")
    if not data:
        abort(400, description="No data provided to update.")
        
    # Allow updating name and/or email
    user.update({k: data[k] for k in ['name', 'email'] if k in data})
    return jsonify({user_id: user})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    if user_id not in users:
        abort(404, description="User not found.")
    deleted = users.pop(user_id)
    return jsonify({"deleted": {"id": user_id, **deleted}})

if __name__ == '__main__':
    app.run(debug=True)
