from functools import wraps
from flask import request, jsonify

def basic_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username and auth.password):
            return jsonify({"error": "Authentication required"}), 401
        # Verify username/password (replace with DB check)
        if auth.username != "admin" or auth.password != "password":
            return jsonify({"error": "Invalid credentials"}), 403
        return f(*args, **kwargs)
    return decorated
