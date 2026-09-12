# Library Management System

A beginner-friendly **Library Management System** developed using Python and Object-Oriented Programming. The application runs through a simple terminal-based menu and provides basic functionality for managing books, issuing and returning books, due dates, and late-return fines. The application is also **containerized using Docker** for consistent execution.

## Features

* Display all books with their availability status
* Issue books to users
* Return issued books
* Add new books to the library
* Automatically record book issue date and time
* Automatically calculate a 14-day due date
* Calculate late-return fines
* Validate book IDs and user inputs
* Prevent duplicate book entries
* Store book names using a text file
* Implemented using Object-Oriented Programming
* Containerized and executed using Docker

## Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **File Handling**
* **Datetime**
* **Exception Handling**
* **Docker**

## Project Structure

```text
library-management-system-python/
│
├── LMS.py
├── list_of_books.txt
├── Dockerfile
└── README.md
```

## Docker

The application is containerized using Docker to provide a consistent Python runtime environment.

### Build the Docker Image

```bash
docker build -t library-management .
```

### Run the Docker Container

```bash
docker run -it library-management
```

The `-it` option allows users to interact with the terminal-based application through the Docker container.
