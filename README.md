# Notes Application

This is a simple web application built using Django that allows users to create, manage, and view personal notes. It includes features for user authentication, CRUD operations for notes, and pagination for easy navigation through multiple notes.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Docker Setup](#docker-setup)


## Features

- User authentication (sign up, log in, log out)
- Create, read, update, and delete notes
- Pagination to view multiple notes easily
- Responsive design using Bootstrap

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django Rest Framework**: For creating RESTful APIs.
- **HTML/CSS**: For frontend development.
- **Bootstrap**: For responsive UI design.
- **Docker**: For containerization of the application.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git
- Docker 

### Local Setup

1. **Clone the Repository:**
   Open your terminal and run:
   ```bash
   git clone https://github.com/dhaminij/notes_app.git
2. **Create a Virtual Environment**
      python -m venv env
3. **Activate the Virtual Environment**
   .\env\Scripts\activate
4. **Install Dependencies**
      pip install -r requirements.txt
5. **Apply Migrations**
      python manage.py migrate
6. **Run the Application**
   python manage.py runserver

 ### Docker Setup

1. **Build the Docker Image:**
   docker build -t mynotes-app .
2. **Run the Docker Container:**
     docker run -d -p 8000:8000 mynotes-app
3. **Access the Application:**
   http://localhost:8000/
4. **Stopping the Container:**
   docker stop <container-id>
   find the container ID by listing all running containers:
   docker ps



   
   
