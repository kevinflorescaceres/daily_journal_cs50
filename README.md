# Daily Journal Flask Application

A simple web application built with Flask to create, read, update, and delete journal entries. This project is part of my CS50 final project.

## Features

- Add new journal entries
- Edit existing journal entries
- Delete journal entries
- View all entries in reverse chronological order

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
