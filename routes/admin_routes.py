from flask import Blueprint, request, jsonify
from models import User, BorrowRequest, BorrowHistory, db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@admin_bp.route('/borrow-requests', methods=['GET'])
def view_borrow_requests():
    requests = BorrowRequest.query.all()
    return jsonify([{
        "id": req.id,
        "user_id": req.user_id,
        "book_id": req.book_id,
        "start_date": req.start_date,
        "end_date": req.end_date,
        "status": req.status
    } for req in requests])

@admin_bp.route('/borrow-requests/<int:request_id>', methods=['PATCH'])
def approve_or_deny_request(request_id):
    data = request.json
    status = data.get('status')
    if status not in ['approved', 'denied']:
        return jsonify({"error": "Invalid status"}), 400

    borrow_request = BorrowRequest.query.get(request_id)
    if not borrow_request:
        return jsonify({"error": "Request not found"}), 404

    borrow_request.status = status
    db.session.commit()
    return jsonify({"message": f"Request {status} successfully"}), 200
