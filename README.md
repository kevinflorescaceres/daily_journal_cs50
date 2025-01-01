# Minimalist Daily Journal App

A simple web application built with Flask to create, read, update, and delete journal entries. This project is part of my CS50 final project.

#### Video Demo: https://www.youtube.com/watch?v=wfbFgQYHD0E
#### Deployed app link: https://kevindelosvientos.pythonanywhere.com/entries/

## Description

The Minimalist Daily Journaling App is a Flask-based web application designed to provide users with a streamlined interface for creating, managing, and deleting journal entries. The project focuses on simplicity and ease of use, adhering to minimalist principles in its functionality and design.

### Features

- Entry Management: Users can create, view, edit, and delete journal entries efficiently.

- Database Integration: SQLite is used as the database backend for storing journal data, ensuring simplicity and portability.

- Responsive Design: The frontend is styled with Bootstrap to provide a clean and responsive user interface.

### Project Structure

- app.py: The primary entry point of the Flask application. Contains the application instance and route definitions.

- db.py: Includes database-related utilities such as establishing connections and initializing the schema.

- entries.py: Manages the core functionality of the application, including routes for CRUD operations on journal entries.

- schema.sql: SQL script defining the structure of the database, including the schema for journal entries.

- templates/: Contains HTML templates rendered by Flask, organized for modularity and reuse.

- static/: Hosts static assets like CSS and JavaScript files.

- wsgi.py: WSGI configuration file used for deployment on platforms like PythonAnywhere.

### Key Design Choices

- Flask Framework: Chosen for its lightweight and modular architecture, enabling rapid development of web applications.

- SQLite Database: Selected for its simplicity and self-contained nature, suitable for small to medium-scale applications.

- Bootstrap Framework: Used to ensure responsive and visually consistent user interface design without extensive custom styling.

### Deployment Process on PythonAnywhere

- Deployment on PythonAnywhere was carried out using the following procedure:

- File Upload: The project files, including Python scripts, templates, and static assets, were uploaded to the PythonAnywhere server either via Git or direct upload.

- Virtual Environment Setup: A Python virtual environment (.venv) was created, and dependencies were installed using pip install -r requirements.txt.

- Database Initialization: The SQLite database was initialized by executing the init_db() function in a Python shell.

- WSGI Configuration: The WSGI file (wsgi.py) was configured to reference the Flask application, enabling PythonAnywhere to serve the app.

- Production Deployment: The web application was activated via PythonAnywhere’s web app dashboard, making it accessible to the public.

### Future Enhancements

- User Authentication: Implement user accounts and authentication to allow personalized and private journaling.

- Tag Filtering: Introduce the ability to filter and categorize journal entries using tags for better organization.

- Enhanced Frontend: Consider integrating more advanced frontend technologies like React or Vue.js for improved interactivity.

### Acknowledgment

This project was developed as the final project for CS50x, showcasing skills in web development, database integration, and deployment. The application provides a functional platform for daily journaling, demonstrating the principles of full-stack development.

## Setup

### Prerequisites

Before setting up the project, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/daily-journal.git
   cd daily-journal
   ```

2. Create a virtual environment:

    ```
    python -m venv .venv
    ```

3. Activate the virtual environment:

    On macOS/Linux:

        source .venv/bin/activate
        

    On Windows:

        .venv\Scripts\activate


4. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Set up the database:

    ```
    flask init-db
    ```
    
    This will initialize the SQLite database.

### Running the Application
To start the Flask application, use the following command:

```
flask run
```

The application will be available at http://127.0.0.1:5000.

### Environment Variables
You can manage your environment variables through the .flaskenv file. The typical settings include:

```
FLASK_APP=app.py
FLASK_ENV=development
```

You can also specify other variables like SECRET_KEY and DATABASE_URI in the .flaskenv file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
