# Real-Time Leaderboard System

## Overview
This project is a backend system for a real-time leaderboard service built with Python, Flask, and Redis. The system allows users to submit scores, view their rankings, and see the top players in real-time.

## Features
- User Authentication (JWT)
- Score submission
- Real-time leaderboard updates using Redis
- View top players
- Check user rank

## Tech Stack
- Python
- Flask (Backend Framework)
- Redis (Leaderboard Storage)
- JWT (Authentication)

## Setup

### Prerequisites
- Python 3.11+
- Redis (Running on port 6379)
- A virtual environment (optional but recommended)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/real-time-leaderboard.git
    cd real-time-leaderboard
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure Redis is running on `localhost:6379`.

5. Start the Flask application:
    ```bash
    flask run
    ```

6. Use Postman or cURL to interact with the API.

## API Endpoints

### 1. Register User
- **POST** `/auth/register`
- Body (JSON):
    ```json
    {
        "username": "testuser",
        "password": "password123"
    }
    ```

### 2. Login User
- **POST** `/auth/login`
- Body (JSON):
    ```json
    {
        "username": "testuser",
        "password": "password123"
    }
    ```

### 3. Submit Score
- **POST** `/leaderboard/submit`
- Body (JSON):
    ```json
    {
        "score": 100
    }
    ```

- **JWT Token Required** in Authorization header.

### 4. Get Top N Players
- **GET** `/leaderboard/top/<int:n>`

### 5. Get Current User's Rank
- **GET** `/leaderboard/rank`
- **JWT Token Required** in Authorization header.
