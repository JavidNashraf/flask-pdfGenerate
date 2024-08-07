# User Management System

This is a simple User Management System built with Flask, SQLAlchemy, and ReportLab. It allows users to add new users, view a list of users, and generate PDF reports of user data.

## Features

- Add new users with name and email
- Display a list of all users
- Generate PDF reports of user data

## Project Structure

- `app/`: Main application package
  - `__init__.py`: Application factory
  - `database.py`: Database configuration
  - `models.py`: User model definition
  - `routes.py`: Route definitions
  - `pdf_generator.py`: PDF generation functionality
- `templates/`: HTML templates
  - `index.html`: Main page template
- `static/`: Static files (CSS, generated PDFs)

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Set up the database:
   - `flask db init`
   - `flask db migrate`
   - `flask db upgrade`
6. Run the application: `flask run`

## Usage

1. Navigate to `http://localhost:5000` in your web browser
2. Use the form to add new users
3. View the list of users on the main page
4. Click the "Generate PDF" link to download a PDF report of all users

## Technologies Used

- Flask: Web framework
- SQLAlchemy: ORM for database management
- ReportLab: PDF generation
- HTML/CSS: Frontend

## Future Improvements

- Add user authentication and authorization
- Implement user editing and deletion functionality
- Add pagination for the user list
- Improve PDF report design and add more data visualization