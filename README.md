# FedditSentiment API

## Overview

This is the FedditSentiment API, a FastAPI-based web API for sentiment analysis on Feddit comments. The API provides endpoint for analyzing sentiment, fetching subfeddits, and fetching comments from the Feddit API.

## Project Structure

The project structure is organized as follows:

```plaintext
FedditSentiment/
├── src/
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── __init__.py
│   ├── auth.py
│   ├── logic.py
│   └── routes.py
├── __init__.py
├── main.py
├── requirements.txt
```
- `src/`: Contains the source code for the project.
  - `tests/`: Directory for test modules.
  - `auth.py`: Module containing authentication-related code.
  - `logic.py`: Module containing business logic for the project.
  - `routes.py`: Module containing the API routes.
- `main.py`: Main module for running the FastAPI application.
- `requirements.txt`: File containing the project dependencies.
- `Dockerfile`: Docker configuration file for containerization.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Roshan835/FedditSentiment.git
```

```bash
cd FedditSentiment
```

2. Install dependencies:

``` bash
pip install -r requirements.txt
```
3. Run the FastAPI application:

```bash
uvicorn main:app --reload
```
OR
```bash
python -m uvicorn main:app --reload
```

Access the API at http://localhost:8000.
Also make sure that the feddit-api docker is running.

4. Enter Authorization code:
   The code is: 12345

# Testing

Run the provided test case:
```bash
pytest src/tests/test_main.py
```
