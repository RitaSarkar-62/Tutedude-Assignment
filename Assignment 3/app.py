from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

# -----------------------------
# MongoDB Atlas Connection
# -----------------------------

MONGO_URI = os.getenv("MONGO_URI")

client = None
collection = None

if MONGO_URI:
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")

        db = client["flask_mongodb_db"]
        collection = db["submissions"]

        print("MongoDB Atlas connected successfully!")

    except Exception as e:
        print("MongoDB connection error:", e)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Task 1: JSON API
# -----------------------------

@app.route("/api")
def api():

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# -----------------------------
# Task 2: Form Submission
# -----------------------------

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="All fields are required."
        )

    if collection is None:
        return render_template(
            "index.html",
            error="MongoDB connection is not available."
        )

    try:

        document = {
            "name": name,
            "email": email,
            "message": message
        }

        collection.insert_one(document)

        return redirect(url_for("success"))

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Error: {str(e)}"
        )


# -----------------------------
# Success Page
# -----------------------------

@app.route("/success")
def success():
    return render_template("success.html")


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)