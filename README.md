
# LinkedIn Simulation (Django Project) Working in progress

## Overview

This is a LinkedIn simulation built using the Django framework. The project aims to provide core functionalities similar to LinkedIn, including user profiles, job postings, connections, and messaging. Please note that this project is still in development, and several key features are yet to be completed.

It should be noted that this project is under development and there is a possibility of disruption, including disruption in some static files.
## Current Status

- **User authentication** (login, signup, logout) is functional.
- **Basic profile creation** is implemented.
- **Home page** with basic feed structure is in place.

  
**Work still to be done:**
- **Post creation** is partially implemented.
- Enhancements to user profiles.
- Implementation of connection requests and network building.
- Messaging between users.
- Job posting and job search functionalities.
- Feed improvements (likes, comments, and shares).
  
## Technologies Used

- **Backend**: Django
- **Frontend**: Django Templates, Bootstrap (for styling), HTML, CSS
- **Database**: SQLite (default with Django)

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Hessam-Hosseinian/django-linkedin.git
    cd django-linkedin
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    # For Windows
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to `http://localhost:8000/`.

## How to Contribute

Since this project is still in development, contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Open a pull request.


