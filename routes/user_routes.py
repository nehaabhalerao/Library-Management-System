from flask import Blueprint, request, jsonify
from models import Book, BorrowRequest, BorrowHistory, db
from datetime import datetime

user_bp = Blueprint('user', __name__)

@user_bp.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    return jsonify([{
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "unique_code": book.unique_code,
        "available": book.available
    } for book in books])

@user_bp.route('/borrow-requests', methods=['POST'])
def request_borrow_book():
    data = request.json
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not user_id or not book_id or not start_date or not end_date:
        return jsonify({"error": "Missing fields"}), 400

    # Check overlapping requests
    overlapping = BorrowRequest.query.filter(
        BorrowRequest.book_id == book_id,
        BorrowRequest.status == 'approved',
        (BorrowRequest.start_date <= end_date) & (BorrowRequest.end_date >= start_date)
    ).first()
    if overlapping:
        return jsonify({"error": "Book already borrowed for the selected period"}), 400

    new_request = BorrowRequest(
        user_id=user_id,
        book_id=book_id,
        start_date=datetime.strptime(start_date, '%Y-%m-%d'),
        end_date=datetime.strptime(end_date, '%Y-%m-%d')
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "Borrow request submitted"}), 201

