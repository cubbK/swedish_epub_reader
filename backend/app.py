from flask import Flask
import sqlite3

con = sqlite3.connect("db.sqlite")

app = Flask(__name__)

@app.route("/")
def root():
    return "<p>Backend running!</p>"

@app.route("/convert_epub_to_text")
def convert_epub_to_text():
    return "<p>Converting</p>"