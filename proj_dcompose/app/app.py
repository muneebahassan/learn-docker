from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        db = mysql.connector.connect(
            host="db",  # Use the service name from docker-compose.yml
            user="root",
            password="secret",
            database="mydb"
        )
        return "Connected to MySQL! 🚀"
    except mysql.connector.Error as err:
        return f"Error: {err}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
