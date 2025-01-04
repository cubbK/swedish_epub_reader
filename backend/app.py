import base64
from flask import Flask
import sqlite3

conection = sqlite3.connect("db.sqlite")
cursor = conection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ebook(title, file)")

def fetch_all_data():
    """Fetch all rows from the SQLite table and process binary fields."""
    conn = sqlite3.connect('db.sqlite')
    conn.row_factory = sqlite3.Row  # Allows column access by name
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ebook")
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to a JSON-compatible format
    result = []
    for row in rows:
        row_dict = {}
        for key in row.keys():
            value = row[key]
            # If the value is binary (bytes), encode it in Base64
            if isinstance(value, bytes):
                row_dict[key] = base64.b64encode(value).decode('utf-8')
            else:
                row_dict[key] = value
        result.append(row_dict)

    return result



app = Flask(__name__)

@app.route("/")
def root():
    return "<p>Backend running!</p>"

@app.route("/list_ebooks")
def list_ebooks():
    data = fetch_all_data()
    return data

@app.route("/convert_epub_to_text")
def convert_epub_to_text():
    return "<p>Converting</p>"