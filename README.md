# **Diagnosify - Symptom Checker Web Application**

Diagnosify is a simple, web-based symptom checker that helps users match their symptoms with possible medical diagnoses. It provides a straightforward user interface for inputting symptoms, comparing them with a database of conditions, and displaying the most likely diagnoses along their risk scores which are represented in 3 colors (green, orange, red).

![Diagnosify Logo/Icon](https://github.com/user-attachments/assets/8dbc8a53-ae6f-4b04-b7e8-e1df115410f6)

---

## **Links**

1. Github: ![](https://github.com/AgentNX/Diagnosify)
2. Docker Hub: ![](https://hub.docker.com/repository/docker/softwareengclass/diagnosify-web/general)
3. wait-for-it : ![](https://github.com/vishnubob/wait-for-it)

---

## **Table of Contents**

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Setup & Configuration](#setup--configuration)
5. [Usage](#usage)
6. [Database Structure](#database-structure)
7. [Security Measures](#security-measures)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Technology Stack](#technology-stack)
11. [License](#license)
12. [Contributors](#contributors)
13. [Acknowledgments](#acknowledgments)

---

## **Overview**

Diagnosify is a web application built with Python (Flask), PostgreSQL, and Docker, aimed at helping users quickly identify potential diagnoses based on the symptoms they provide. The app uses a simple algorithm to match symptoms with medical conditions. This application is intended to be lightweight, easy to use, and run in both development and production environments.

---

## **Features**

* **Symptom Matching:** Users can input a list of symptoms, and the app matches them with potential medical conditions stored in the database.
* **Symptom Risk Level (Badge Color):** Depending on how many of the symptoms match a diagnosis/illness the color of the badges will be different.
* **User Interface:** A simple, user-friendly interface built with HTML and CSS that allows easy input and display of results.
* **Database Logging:** All user-submitted symptoms and results are saved in a PostgreSQL database for logging and future analysis.

![Result](https://github.com/user-attachments/assets/69999250-8496-4242-a935-a2482e448adb)

---

## **Installation**

### Prerequisites

* Python 3.x
* PostgreSQL
* Docker (optional for deployment)

### Steps to Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AgentNX/Diagnosify.git
   cd Diagnosify
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## **Setup & Configuration**

### Database Setup

1. **Create and configure the PostgreSQL database**:

   * If PostgreSQL is not installed, you can install it or use Docker to spin up a container with PostgreSQL.

   * Create the `symptoms` database and configure it to match the application.

   ```bash
   psql -U postgres
   CREATE DATABASE symptoms;
   ```

2. **Configure Database URL:**
   Set up the PostgreSQL connection URL in your `.env` file:

   ```
   DATABASE_URL=postgresql://username:password@localhost/symptoms
   ```

3. **Run Migrations:**

   ```bash
   flask db upgrade
   ```

![DB](https://github.com/user-attachments/assets/9d0a19ad-9800-4036-8913-d23310c33313)

---

## **Usage**

### Running the App Locally

To run the application in development mode:

1. **Start the Flask development server:**

   ```bash
   flask run
   ```

2. **Access the application in your browser:**
   Navigate to `http://127.0.0.1:5000/` to interact with the application.

![Main](https://github.com/user-attachments/assets/e1f3a2ad-7859-4225-9a0e-44186fb396a7)

### Docker Deployment

Diagnosify is also Dockerized for easy deployment in a containerized environment.

1. **Build the Docker images:**

   ```bash
   docker-compose up --build
   ```

2. **Access the application via Docker:**
   Once the app is up and running in Docker, you can access it through `http://localhost:5000/`.

![Main](https://github.com/user-attachments/assets/e1f3a2ad-7859-4225-9a0e-44186fb396a7)

---

## **Database Structure**

Diagnosify uses PostgreSQL to store user-submitted symptoms and diagnosis results.

### **symptom\_log Table**

* `id`: Integer (Primary Key) – Unique identifier for each log entry.
* `symptom`: String (120 characters) – The symptom inputted by the user.
* `matched_condition`: String (120 characters) – The condition that was matched to the symptom.
* `timestamp`: DateTime – The date and time when the symptom was logged.

![DB Structure](https://github.com/user-attachments/assets/8d018a62-0411-48cb-91dc-b485f2a251e2)

---

## **Security Measures**

Several basic security measures have been implemented in the app to ensure data safety and integrity:

* **Environment Variables:** Sensitive data such as the database credentials are stored in an `.env` file.
* **Input Validation:** User inputs are sanitized to avoid basic injection attacks.
* **HTTPS:** Although not fully set up in this version, HTTPS can be configured for production deployments.
* **Docker Security:** The app runs in isolated Docker containers to minimize security risks.

---

## **Testing**

The project includes basic unit tests and can be expanded for comprehensive testing. To run tests:

```bash
pytest
```

![PyTest](https://github.com/user-attachments/assets/9da6107f-1d4e-433e-b363-8600864dacfd)

Make sure your environment is set up correctly, and all dependencies are installed before running the tests.

---

## **Deployment**

### Docker Deployment

To deploy Diagnosify using Docker, follow the steps:

1. **Build the Docker images:**

   ```bash
   docker-compose up --build
   ```

2. **Run the containers:**

   ```bash
   docker-compose up
   ```

   After this, the app will be available on `http://localhost:5000/`.

---

## **Technology Stack**

* **Backend:** Python 3.x, Flask
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS
* **Containerization:** Docker
* **ORM:** SQLAlchemy
* **Web Server:** Gunicorn (for production deployments)

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contributors**

* **AgentNX** - Lead Developer

Feel free to fork the repository, contribute, or open issues if you have any questions or suggestions.

---

## **Acknowledgments**

* **Flask:** Lightweight web framework for building the app.
* **SQLAlchemy:** ORM used to interact with the PostgreSQL database.
* **PostgreSQL:** Used as the relational database for storing symptoms and diagnoses.

---

## Main Page
![image](https://github.com/user-attachments/assets/fb069216-be51-48ac-bf08-c65d1d2c63de)

## Result Page
![image](https://github.com/user-attachments/assets/5f456ac3-3e84-4964-b2f4-b5fa88b546f4)
