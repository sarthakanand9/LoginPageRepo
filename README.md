# 🚀 Dockerized Flask + MySQL Login App

This is a simple full-stack web application built using:

- 🐍 Flask (Python backend)
- 🐬 MySQL (Database)
- 🐳 Docker & Docker Compose

The app allows users to enter their **Name** and **Email**, and stores the data in a MySQL database.

---

# 📁 Project Structure


login-docker-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── templates/
└── index.html


---

# ⚙️ Prerequisites

Make sure you have installed:

- Docker
- Docker Compose

---

# ▶️ How to Run the Project

## Step 1: Clone Repository

```bash
Step 1: Clone Repository

git clone https://github.com/sarthakanand9/login-docker-app.git

cd login-docker-app

Step 2: Start Containers

    docker-compose up --build


Step 3: Open in Browser

    http://localhost:5000

🧠 How It Works

    Flask runs inside a Docker container
    MySQL runs in a separate container
    Flask connects to MySQL using service name db
    On form submission:
    Table is created (if not exists)
    Data is inserted into database

🗄️ Database Details

    Database Name: userdb
    Table Name: users
    Table Schema:
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    );
    🔍 How to Check Stored Data (MySQL in Docker)

Step 1: Check Running Containers

    docker ps

👉 Copy the MySQL container ID (for service db)

Step 2: Access MySQL Container

    docker exec -it <container_id> mysql -u root -p

👉 Enter password:
root

Step 3: Use Database

    USE userdb;
    Step 4: View Data
    SELECT * FROM users;

🎉 You will see all submitted Name & Email records here.

🐳 Docker Services

    Web (Flask App)
    Builds from Dockerfile
    Runs on port 5000
    DB (MySQL)
    Image: mysql:5.7
    Port: 3307 (external) → 3306 (internal)


🔧 Useful Commands
    Stop Containers
    docker-compose down
    Rebuild Containers
    docker-compose up --build
    Check Logs
    docker-compose logs