# API Automation Framework

## Project Overview

This project is a REST API automation framework built using Python, pytest, and requests.

It demonstrates API testing for GET, POST, PUT, and DELETE operations using the ReqRes API.

---

## Tech Stack

* Python
* pytest
* requests
* GitHub
* GitHub Actions

---

## Project Structure

```
api-automation-framework/
│
├── config/
│   └── config.py
│
├── .github/workflows/
│   └── tests.yml
│
├── utils/
│   ├── api_client.py
│   └── logger.py
│
├── tests/
│   └── test_users.py
│
├── logs/              # generated at runtime (ignored in git)
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Test Coverage

* GET user
* CREATE user (POST)
* UPDATE user (PUT)
* DELETE user (DELETE)

---

## Pytest Configuration
The project uses `pytest.ini` to define test discovery paths and configuration.

---

## CI/CD
GitHub Actions workflow is implemented to automatically execute Pytest-based test suites on each code push, ensuring continuous validation of API functionality.

---

## How to Run Tests

### 1. Create virtual environment

```
python -m venv venv
```

### 2. Activate environment

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run tests

```
pytest
```

---

## Features

* Reusable API client
* Centralized configuration
* Logging support
* Clean test structure

---

## Future Improvements

* Environment configuration (dev/staging)
* Advanced reporting

---

## Author

Hoa Mai
