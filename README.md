# User Authentication with FastAPI

This project is a user authentication system built using FastAPI, MongoDB, and JWT (JSON Web Tokens). It includes user registration, secure password hashing, and token-based authentication with JWT.

## Features

- **User Registration**: Register new users with username, company, and hashed password stored in MongoDB.
- **User Login**: Authenticate users with JWT, allowing secure and stateless session handling.
- **Password Hashing**: Uses bcrypt hashing for storing secure passwords.
- **Token Generation**: Generates JWT access tokens for authenticated users.

## Technologies Used

- **Backend Framework**: FastAPI
- **Database**: MongoDB
- **Token-based Authentication**: JWT
- **Password Hashing**: bcrypt
- **Frontend**: React (with Axios for API requests)
- **Environment Management**: Python virtual environment

## Project Structure

```plaintext
User-authentication-fastapi
├── backend
│   ├── main.py              # FastAPI main application
│   ├── hashing.py           # Password hashing utilities
│   ├── jwttoken.py          # JWT creation and verification
│   ├── oauth.py             # OAuth2 token management
│   └── venv                 # Virtual environment for project dependencies
└── frontend
    ├── App.js               # Main React application with login form
    ├── components           # React components, if applicable
    ├── package.json         # Frontend dependencies
    └── public               # Public files for the frontend
```
## Setup and Installation

### Prerequisites

Before setting up the project, ensure you have the following tools installed:

- Python 3.7+
- MongoDB (local or cloud via MongoDB Atlas)
- Node.js (for frontend, if applicable)
- Git (for version control)

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/drethikapila/User-authentication-fastapi.git
   cd User-authentication-fastapi

2. **Set up the Python virtual environment**:
   ```bash
   python -m venv venv

3. **Activate the virtual environment**:
   ```bash
   venv\Scripts\activate

4. **Install required dependencies**:

5. **Configure MongoDB**:

Set up MongoDB and connect it to your FastAPI app. You can use a local MongoDB instance or a cloud MongoDB provider like MongoDB Atlas.
Set your MongoDB URI in the backend code (typically inside main.py) to establish the connection.

6. **Run the FastAPI application**:
   ```bash
   uvicorn backend.main:app --reload

Your FastAPI app will be running on http://127.0.0.1:8000.

### Frontend Setup
1. **Navigate to the frontend directory**:
   ```bash
   cd frontend

2. **Install dependencies**:
   ```bash
   npm install

3. **Run the React app**:
   ```bash
   npm start

The React app will be running on http://localhost:3000.

### Environment Variables Setup
The credentials for the MongoDB connection and other sensitive information should be stored in a .env.local file, which is not tracked by Git for security reasons.

1. **Create a .env.local file in the root of the project directory**.

You can base the file on the .env.local file provided in the repository (if you include one), or you can create it manually. Here's an example of what the file should look like:

```bash
USERNAME=your_mongo_username
PASSWORD=your_mongo_password

2. **Add your MongoDB credentials**




