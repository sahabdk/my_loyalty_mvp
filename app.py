from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Just a test route to confirm our app runs
@app.route("/")
def home():
    return "Hello, this is my loyalty MVP!"

# Example of connecting to the database (optional right now)
@app.route("/test-db")
def test_db():
    # Read environment variable for DB URL
    db_url = os.environ.get("DATABASE_URL", "")
    if not db_url:
        return "DATABASE_URL not found! Did you set it?"

    # Try a simple DB connection
    try:
        with psycopg2.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
        return f"Connected! PostgreSQL version: {version}"
    except Exception as e:
        return f"DB connection error: {str(e)}"

if __name__ == "__main__":
    # Run Flask locally on port 8080
    app.run(host="0.0.0.0", port=8080)
