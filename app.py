from flask import Flask, render_template, request
import mysql.connector
import time

app = Flask(__name__)

# Retry DB connection (important for Docker)
def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",  # service name from docker-compose
                user="root",
                password="root",
                database="userdb"
            )
            return conn
        except:
            print("Waiting for MySQL...")
            time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
    """)

    # ✅ Insert data
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)