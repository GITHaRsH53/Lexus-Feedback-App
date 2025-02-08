Python Flask Feedback App

This is a Flask-based Feedback Application that allows users to submit feedback, which is then stored in a PostgreSQL database and sent via email notifications. The app is developed using Flask, SQLAlchemy ORM, and Mailtrap.io for email testing. It follows the Model-View-Controller (MVC) architecture and utilizes Object-Oriented Programming (OOP) principles for structuring the database models and backend logic. The frontend is built using HTML, CSS, and Flask templates, ensuring a clean and user-friendly interface.

🔹 Key Features

📝 Feedback Form: Users can submit feedback including customer name, dealer name, rating, and comments.

📄 Data Storage: Feedback is stored in a PostgreSQL database using SQLAlchemy ORM.

📩 Email Notifications: After submission, the feedback details are sent via email using SMTP protocol and Mailtrap.io.

🚀 Flask-Based Backend: Routes are defined in app.py, handling user requests and managing the database.

🔍 Validation & Error Handling:
    Ensures required fields are filled.
    Prevents duplicate feedback submissions.

🔧 Environment Configuration:
    Development Mode (dev): Debugging enabled, database connected.
    Production Mode: Debugging disabled, connection settings hidden.

🎨 Frontend Design: Uses HTML, CSS, and Flask Jinja Templates to render dynamic content.

🔹 Technologies Used

Flask – Web framework for handling routes and requests.

PostgreSQL – Database for storing feedback.

SQLAlchemy – ORM for database interactions.

Mailtrap.io – Testing SMTP email service.

HTML & CSS – For frontend design.

🔹 How It Works
User submits feedback through a form on the index.html page.
The backend processes the request, validates input, and checks for duplicate feedback.
If valid, the feedback is stored in the PostgreSQL database using SQLAlchemy.
An email notification with the feedback details is sent using Mailtrap.io SMTP service.
The user is redirected to a success page or an error message is displayed if the input is invalid.

This project provides a simple yet powerful feedback management system using Flask and PostgreSQL, making it easy to collect, store, and process customer feedback efficiently. 🚀🔥