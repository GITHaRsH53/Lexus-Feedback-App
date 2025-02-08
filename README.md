# **Python Flask Feedback App**

This is a __Flask-based Feedback Application__ that allows users to submit feedback, which is then stored in a __PostgreSQL database__ and sent via __email notifications__. The app is developed using ___Flask, SQLAlchemy ORM,__ and __Mailtrap.io__ for email testing. It follows the __Model-View-Controller (MVC) architecture__ and utilizes __Object-Oriented Programming (OOP)__ principles for structuring the database models and backend logic. The frontend is built using __HTML, CSS, and Flask templates,__ ensuring a clean and user-friendly interface.

## 🔹 __Key Features__

📝 __Feedback Form__: Users can submit feedback including customer name, dealer name, rating, and comments.

📄 __Data Storage__: Feedback is stored in a __PostgreSQL database__ using SQLAlchemy ORM.

📩 __Email Notifications__: After submission, the feedback details are sent via email using __SMTP protocol__ and __Mailtrap.io__.

🚀 __Flask-Based Backend__: Routes are defined in app.py, handling user requests and managing the database.

🔍 __Validation & Error Handling__:
    Ensures required fields are filled.
    Prevents duplicate feedback submissions.

🔧 __Environment Configuration__:
    Development Mode (dev): Debugging enabled, database connected.
    Production Mode: Debugging disabled, connection settings hidden.

🎨 __Frontend Design__: Uses __HTML, CSS__, and __Flask Jinja Templates__ to render dynamic content.

## 🔹 __Technologies Used__

__Flask__ – Web framework for handling routes and requests.

__PostgreSQL__ – Database for storing feedback.

__SQLAlchemy__ – ORM for database interactions.

__Mailtrap.io__ – Testing SMTP email service.

__HTML & CSS__ – For frontend design.

## 🔹 __How It Works__
User submits feedback through a form on the __index.html__ page.
The backend processes the request, validates input, and checks for duplicate feedback.
If valid, the feedback is stored in the ___PostgreSQL database__ using SQLAlchemy.
An email notification with the feedback details is sent using __Mailtrap.io SMTP service__.
The user is redirected to a success page or an error message is displayed if the input is invalid.

This project provides a __simple yet powerful feedback management system__ using __Flask and PostgreSQL,__ making it easy to collect, store, and process customer feedback efficiently. 🚀🔥