# Service API

Completed task for the vacancy.
https://hh.ru/

## Table of Contents:

    1. Introduction
    2. Features
    3. Installation
    4. Usage
    5. API Endpoints
    6. Python Best Practices
    7. API Best Practices

## Introduction

In this task, I implemented the API of a server that keeps track of services and their states.

## Features

    1. FastAPI framework for real execution speed
    2. Dependency Injection to ensure low code cohesion
    3. MongoDB as a database
    4. Validation models for data integrity in non-relational mongo

## Installation

List of steps required to set up and run project.

```bash
git clone https://github.com/skeesh24/service-api.git

cd serviceapi

python -m venv venv

venv\Scripts\activate  # On Linux: source venv/bin/activate

pip install -r requirements.txt
```

## Usage

Next, you should start the server.

```bash
python3 src/main.py
```

## API Endpoints

Detail the available API endpoints:

### GET /services

This route returns a list of all existing services.

Example:

```bash
GET http://localhost:8888/service
```

### GET /services/{name}

This route returns the service by its name provided as a query parameter.

Example:

```bash
GET http://localhost:8888/service/redis
```

### POST /services

This route adds a new service to the database. You can use the test-dump.json file to quickly fill the body of the POST request.

Example:

```bash
POST http://localhost:8888/service
Content-Type: application/json

{
    "service": "NewService",
    "status": "enabled",
    "description": "A new service"
}
```

## Python Best Practices

    1. Used a virtual environment to manage dependencies.
    2. Followed PEP 8 style guide for code formatting.
    3. Handle exceptions gracefully and provide meaningful error messages.
    4. Used interfaces to

## API Best Practices

    1. Use RESTful conventions for API design.
    2. Keep endpoints and resource names descriptive.
    3. Use HTTP status codes appropriately (e.g., 200 for success, 404 for not found, 400 for bad requests, etc.).
    4. Validate input data and provide meaningful validation error responses.
    4. Secure sensitive data and endpoints with authentication and authorization as needed.

## Warning

There is also an .env file in the repository.
Since creating a new MongoDB cluster is time consuming, I decided to leave the environment file ready.
