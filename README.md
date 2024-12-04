# **Library Management System**  

## **Overview**  
The Library Management System is a backend API built with Python to manage library operations efficiently. It allows admins to handle users, books, and borrow requests, while users can view available books, make borrowing requests, and check their history. The system ensures secure access and prevents overlapping book borrow requests.  

---

## **Features**  
### **Admin (Librarian):**  
- Create and manage library users.  
- Approve or deny book borrow requests.  
- View a user’s borrowing history.  

### **Library Users:**  
- Browse and view available books.  
- Submit book borrow requests with specific dates.  
- Check their personal borrowing history.  

### **System Highlights:**  
- Prevents double-booking of the same book during overlapping periods.  
- Implements secure authentication for all API endpoints.  
- Handles edge cases such as invalid data or non-existent users/books.  

---

## **Technologies Used**  
- **Backend Framework:** Flask / FastAPI  
- **Database:** SQLite (using SQLAlchemy ORM)  
- **Authentication:** Basic Authentication (extendable to JWT)  
- **Language:** Python  

---

## **Setup and Installation**  

### **Prerequisites:**  
1. Python 3.x installed on your system.  
2. Git installed to clone the repository.  

### **Steps to Set Up:**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/nehaabhalerao/library-management-system.git
   cd library-management-system
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:  
   ```bash
   python database.py
   ```
4. Run the application:  
   ```bash
   python app.py
   ```
5. Access the APIs at `http://localhost:5000`.  

---

## **API Documentation**  

### **Admin APIs:**  
1. `POST /admin/users`  
   - **Description:** Create a new library user.  
   - **Request Body:**  
     ```json
     {
       "email": "user@example.com",
       "password": "password123"
     }
     ```  

2. `GET /admin/borrow-requests`  
   - **Description:** View all pending borrow requests.  

3. `PATCH /admin/borrow-requests/<id>`  
   - **Description:** Approve or deny a borrow request.  
   - **Request Body:**  
     ```json
     {
       "status": "approved"  // or "denied"
     }
     ```  

4. `GET /admin/users/<id>/history`  
   - **Description:** View borrowing history of a specific user.  

### **User APIs:**  
1. `GET /users/books`  
   - **Description:** Get a list of all available books.  

2. `POST /users/borrow-requests`  
   - **Description:** Submit a request to borrow a book.  
   - **Request Body:**  
     ```json
     {
       "book_id": 1,
       "start_date": "2024-12-01",
       "end_date": "2024-12-10"
     }
     ```  

3. `GET /users/history`  
   - **Description:** View the user's personal borrowing history.  

---

## **Future Enhancements**  
- Replace Basic Authentication with JWT for better security.  
- Add a feature for users to download borrowing history as a CSV file.  
- Develop a frontend UI for better user experience.  

---

## **License**  
This project is licensed under the [MIT License](LICENSE).  

---

## **Contact**  
- Developer:Neha Bhalerao 
- GitHub:(https://github.com/nehaabhalerao)  
