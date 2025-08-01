# 🎓 Student Results Portal

A **Full Stack Web Application** built with **Flask** and **PostgreSQL**, designed to help students view their academic results by entering their details such as hall ticket number, semester, and more.

---

## 🔍 Features

- 🔑 Student login with Hall Ticket & other academic details
- 📄 Subject-wise result display
- ⚠️ Intelligent failure detection
- 🔁 Reattempt/reappear result tracking
- 🧾 Memo page generation for exam attempts
- 🎯 Clean and user-friendly interface

---

## 🛠️ Built With

- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Jinja2 Templates

---

## 📁 Folder Structure
Student-Results-Portal/
│
├── templates/ # HTML templates (index.html, result.html, memo.html)
├── static/ # CSS or JS files (if any)
├── app.py # Flask application
├── requirements.txt # Dependencies
├── Procfile # For deployment
└── README.md # Project documentation

---

## 🚀 How to Run Locally

### Prerequisites:
- Python 3.x
- PostgreSQL
- pip (Python package installer)
### clone the repository
'''bash
git clone https://github.com/Bhavana0517b/Student-Results-Portal.git
cd Student-Results-Portal

2.install dependencies:
pip install -r requirements.txt

3.Set up PostgreSQL:
Create a PostgreSQL database named students
Import your data into a table named students_info

Update the app.py with your DB credentials:
DB_HOST = 'localhost'
DB_NAME = 'students'
DB_USER = 'postgres'
DB_PASS = 'your_password'

4.Run the Flask App:
python app.py
Visit http://localhost:1000 in your browser.
