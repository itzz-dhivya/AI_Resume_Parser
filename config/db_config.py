import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_conn():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("AIVEN_HOST"),
            port=int(os.getenv("AIVEN_PORT")),  # ✅ Convert to int
            user=os.getenv("AIVEN_USER"),
            password=os.getenv("AIVEN_PASSWORD"),
            database=os.getenv("AIVEN_DB"),
            ssl_ca="config/ca.pem",  # Make sure ca.pem is in config/ folder
            ssl_verify_cert=True
        )

        if conn.is_connected():
            print("✅ Connected to Aiven MySQL via .env successfully!")
            return conn
        else:
            print("⚠️ Connection failed.")
            return None

    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None
