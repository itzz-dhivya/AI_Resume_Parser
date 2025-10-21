import streamlit as st
import mysql.connector
from mysql.connector import Error
import os

def get_conn():
    try:
        # Save SSL cert (needed for Aiven)
        if "SSL_CA" in st.secrets:
            with open("aiven_cert.pem", "w") as f:
                f.write(st.secrets["SSL_CA"])
            ssl_path = "aiven_cert.pem"
        else:
            ssl_path = None

        # Connect to Aiven MySQL
        conn = mysql.connector.connect(
            host=st.secrets["AIVEN_HOST"],
            port=int(st.secrets["AIVEN_PORT"]),
            user=st.secrets["AIVEN_USER"],
            password=st.secrets["AIVEN_PASSWORD"],
            database=st.secrets["AIVEN_DB"],
            ssl_ca=ssl_path,
            ssl_verify_cert=True
        )

        if conn.is_connected():
            print("✅ Connected to Aiven MySQL via Streamlit Secrets successfully!")
            return conn
        else:
            print("⚠️ Connection failed.")
            return None

    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None
