import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Create and return a PostgreSQL database connection."""

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database connection successful!")
        conn.close()
    except Exception as e:
        print("Database connection failed:")
        print(e)