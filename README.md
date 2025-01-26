# Task Management API

![Logo](https://res.cloudinary.com/geetechlab-com/image/upload/v1737920676/githubs/TaskAPI_gyxenf.png)

A Task Management API built using Django to help you efficiently organize and manage tasks. This document provides steps to get the API up and running smoothly using Docker or virtual environments.

---

## Prerequisites

Ensure the following are installed on your system:

- Docker (if using Docker Compose)
- Python 3.8 or later (if using virtual environment)
- pip (Python package manager)
- Git

---

## Getting Started

You can run this API using **Docker Compose** or by setting up a **virtual environment** manually. Choose the method that works best for you.

---

### Option 1: Run with Docker Compose

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a `.env` file in the root directory and provide the following values:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_BACKEND=your_email_backend
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_host_user
   EMAIL_HOST_PASSWORD=your_email_host_password
   EMAIL_USE_SSL=True
   SUPPORT_EMAIL=your_support_email
   DEFAULT_FROM_EMAIL=your_default_from_email
   ```

3. Run the Docker Compose command:
   ```bash
   docker-compose up --build
   ```

4. Your API should now be running. Access it at `http://localhost:8000/`.

---

### Option 2: Run with Virtual Environment

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and provide the following values:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_BACKEND=your_email_backend
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_host_user
   EMAIL_HOST_PASSWORD=your_email_host_password
   EMAIL_USE_SSL=True
   SUPPORT_EMAIL=your_support_email
   DEFAULT_FROM_EMAIL=your_default_from_email
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Your API should now be running. Access it at `http://127.0.0.1:8000/`.

---

## Notes

- Replace `your_secret_key` and other placeholders with actual values in the `.env` file.
- Use strong and secure credentials for production.
- Ensure Docker and Python are properly configured before starting.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy Task Management! 🎉
