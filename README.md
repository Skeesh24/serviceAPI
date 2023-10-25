# Service API

Completed task for the vacancy.
https://tyumen.hh.ru/vacancy/88451637

## Table of Contents:

    1. Introduction
    2. Features
    3. Installation
    4. Usage
    5. API Endpoints
    6. Python Best Practices
    7. API Best Practices
    8. Warning

## Introduction

I implemented the API of a server that keeps track of services and their states in this task.

## Features

    1. FastAPI framework for real execution speed
    2. Dependency Injection to ensure low code cohesion
    3. MongoDB as a database
    4. Validation models for data integrity in non-relational mongo
    5. SLA metrics: [Uptime = (Total Time - Disabletime - Unstabletime) / Total Time * 100] and [Availability = (Total Time - Disabletime) / Total Time * 100]

## Installation

List of steps required to set up and run project.

```bash
git clone https://github.com/skeesh24/serviceAPI.git

cd serviceAPI

python3 -m venv venv

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

### GET /service

This route returns a list of all existing services and thier states.

Example:

```bash
GET http://localhost:8888/service
```

### POST /services

This route adds a new service to the database. You can use the test-dump.json file to quickly fill the body of your POST request.

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

### GET /service/{name}?start=...&end=...

This route returns the service statistic by provided name and time interval.
If the start and end parameters are not specified then used a default 12 hour time interval

Example:

```bash
GET http://localhost:8888/service/redis?start=2023-10-26T16:55:46.838+00:00&end=2023-10-26T04:55:46.838+00:00
```

### GET /service/log/{name}

This route returns the service history changes and all the data by provided name. 

Example:

```bash
GET http://localhost:8888/service/log/redis
```

## Python Best Practices

    1. Used a virtual environment to manage dependencies.
    2. Followed PEP 8 style guide for code formatting.
    3. Handle exceptions gracefully and provide meaningful error messages.
    4. Used interfaces to improved code readability and maintainability

## API Best Practices

    1. Used RESTful conventions for API design.
    2. Endpoints and resource names are descriptive.
    3. Use HTTP status codes appropriately (e.g., 200 for success, 404 for not found, 400 for bad requests).
    4. Validate input data and provide meaningful validation error responses.

## Warning

There is also an .env file in the repository.
Since creating a new MongoDB cluster is time consuming, I decided to leave the environment file ready.
