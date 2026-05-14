from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from model_predict import predict_disease

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

app.secret_key = "supersecretkey"

UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# ---------- DATABASE CONNECTIONS ----------
def get_auth_db():
    return sqlite3.connect("auth.db")

def get_feedback_db():
    return sqlite3.connect("feedback.db")


# ---------- CREATE TABLES ----------
with get_auth_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

with get_feedback_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            accuracy TEXT,
            comment TEXT
        )
    """)


# ---------- HELPERS ----------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_hospitals(location):
    data = {
        "Delhi": [
            {"name": "AIIMS Delhi", "phone": "+91-11-26588500"},
            {"name": "Apollo Hospital Delhi", "phone": "+91-11-26925858"},
            {"name": "Fortis Escorts Heart Institute", "phone": "+91-11-47135000"},
            {"name": "Max Super Specialty Hospital", "phone": "+91-11-40554055"}
        ],
        "Mumbai": [
            {"name": "Tata Memorial Hospital", "phone": "+91-22-24177000"},
            {"name": "Kokilaben Dhirubhai Ambani Hospital", "phone": "+91-22-42696969"},
            {"name": "Lilavati Hospital", "phone": "+91-22-26751000"},
            {"name": "Nanavati Super Specialty Hospital", "phone": "+91-22-26267500"}
        ],
        "Bangalore": [
            {"name": "Manipal Hospital", "phone": "+91-80-25024444"},
            {"name": "Fortis Hospital Bangalore", "phone": "+91-80-66214444"},
            {"name": "Narayana Health City", "phone": "+91-80-22122212"},
            {"name": "Apollo Hospital Bannerghatta", "phone": "+91-80-26304050"}
        ],
        "Chennai": [
            {"name": "Apollo Hospitals Chennai", "phone": "+91-44-28293333"},
            {"name": "MIOT International", "phone": "+91-44-42002288"},
            {"name": "Fortis Malar Hospital", "phone": "+91-44-42892222"}
        ],
        "Hyderabad": [
            {"name": "Yashoda Hospitals", "phone": "+91-40-45674567"},
            {"name": "Care Hospitals", "phone": "+91-40-67222222"},
            {"name": "Apollo Hospitals Jubilee Hills", "phone": "+91-40-23607777"}
        ],
        "Pune": [
            {"name": "Ruby Hall Clinic", "phone": "+91-20-26163391"},
            {"name": "Sahyadri Hospital", "phone": "+91-20-67213000"},
            {"name": "Jehangir Hospital", "phone": "+91-20-66819999"}
        ],
        "Kolkata": [
            {"name": "Apollo Gleneagles Hospital", "phone": "+91-33-23203040"},
            {"name": "AMRI Hospitals Dhakuria", "phone": "+91-33-66800000"},
            {"name": "Fortis Hospital Anandapur", "phone": "+91-33-66284444"},
            {"name": "Peerless Hospital", "phone": "+91-33-40111222"}
        ]
    }
    return data.get(location, [])


# ---------- ROUTES ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            return "Passwords do not match"

        hashed = generate_password_hash(password)

        try:
            with get_auth_db() as db:
                db.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (name, email, hashed)
                )
            return redirect("/login")
        except:
            return "Email already exists"

    return render_template("register.html")


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_auth_db()
        user = db.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()

        if user and check_password_hash(user[3], password):
            session["user_id"] = user[0]
            session["user_name"] = user[1].title()  # ✅ FULL NAME STORED
            return redirect("/dashboard")

        return "Invalid login credentials"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    # ✅ FIXED VARIABLE NAME
    return render_template(
        "dashboard.html",
        username=session["user_name"]
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        file = request.files.get("image")
        if not file or file.filename == "":
            return "No file selected"

        if not allowed_file(file.filename):
            return "Invalid file type"

        location = request.form.get("location")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        disease, confidence = predict_disease(filepath)
        hospitals = get_hospitals(location)

        return render_template(
            "result.html",
            image=filename,
            disease=disease,
            confidence=confidence,
            hospitals=hospitals
        )

    return render_template("predict.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        accuracy = request.form["accuracy"]
        comment = request.form["comment"]

        with get_feedback_db() as db:
            db.execute(
                "INSERT INTO feedback (accuracy, comment) VALUES (?, ?)",
                (accuracy, comment)
            )

        return "✅ Feedback submitted successfully!"

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
