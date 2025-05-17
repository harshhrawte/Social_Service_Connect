# Social_Service_Connect

Social_Service_Connect is a basic Flask web application that bridges the gap between NGOs and volunteers. It facilitates NGO posts requesting donations and volunteer drives, while enabling individuals to donate items or sign up to volunteer for events like beach cleanups. The platform helps streamline donation drives and volunteering efforts, fostering greater community participation and social impact.

---

## 📝 Project Description

This project connects NGOs and volunteers by allowing NGOs to post donation needs and volunteer opportunities. Users can donate items, sign up for volunteer events, and engage with the community to support various social causes. The app uses Flask for backend, MySQL for database management, and HTML/CSS for the front-end interface.

---

## ⚙️ Features

- User registration and login system  
- NGOs can post donation requests and volunteer events  
- Volunteers can view and participate in donation drives and volunteer activities  
- Donation form to submit donor details and donated items  
- Simple, user-friendly web interface  

---

## 📦 Requirements

- Python 3.7+  
- Flask  
- Flask-MySQLdb  
- MySQL Server  
- HTML & CSS (frontend templates)  

---

## 🚀 Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/harshhrawte/Social_Service_Connect.git
cd Social_Service_Connect

python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

pip install flask flask-mysqldb

Set up your MySQL database:

Create a database named donaters

Create necessary tables (donate_details, signup, inter, etc.) as per your app requirements.

Update the database credentials in app.py if needed:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'donaters'

python app.py

http://127.0.0.1:5000/


