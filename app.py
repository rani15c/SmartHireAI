from flask import Flask, render_template, request, redirect, session
from database import get_connection, create_table
from rules import evaluate_candidate

app = Flask(__name__)

app.secret_key = "smarthire-secret-key"

create_table()


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CANDIDATE SCREENING ----------------

@app.route("/screen", methods=["POST"])
def screen_candidate():

    name = request.form["name"]
    email = request.form["email"]
    qualification = request.form["qualification"]
    experience = int(request.form["experience"])
    specialization = request.form["specialization"]

    score, status, reasons = evaluate_candidate(
        qualification,
        experience,
        specialization
    )

    connection = get_connection()

    cursor = connection.execute("""
        INSERT INTO candidates
        (name, email, qualification, experience,
         specialization, score, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        email,
        qualification,
        experience,
        specialization,
        score,
        status
    ))

    candidate_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return render_template(
        "result.html",
        name=name,
        score=score,
        status=status,
        reasons=reasons,
        candidate_id=candidate_id
    )


# ---------------- AI CHATBOT ----------------

@app.route("/chatbot/<int:candidate_id>", methods=["GET", "POST"])
def chatbot(candidate_id):

    connection = get_connection()

    candidate = connection.execute("""
        SELECT * FROM candidates
        WHERE id = ?
    """, (candidate_id,)).fetchone()

    connection.close()

    if candidate is None:
        return "Candidate not found", 404

    if request.method == "GET":
        return render_template(
            "chatbot.html",
            candidate=candidate
        )

    answers = [
        request.form["q1"],
        request.form["q2"],
        request.form["q3"],
        request.form["q4"],
        request.form["q5"]
    ]

    keywords = [
        "teaching",
        "students",
        "learning",
        "technology",
        "explain",
        "knowledge",
        "experience",
        "research",
        "practical",
        "project"
    ]

    interview_score = 0

    for answer in answers:

        answer_lower = answer.lower()

        for keyword in keywords:

            if keyword in answer_lower:
                interview_score += 2

    if interview_score > 100:
        interview_score = 100

    if interview_score >= 70:
        interview_status = "Strong Interview Performance"
    elif interview_score >= 40:
        interview_status = "Good Interview Performance"
    else:
        interview_status = "Needs Further Review"

    connection = get_connection()

    connection.execute("""
        UPDATE candidates
        SET interview_score = ?,
            interview_status = ?
        WHERE id = ?
    """, (
        interview_score,
        interview_status,
        candidate_id
    ))

    connection.commit()
    connection.close()

    return render_template(
        "chatbot_result.html",
        candidate=candidate,
        interview_score=interview_score,
        interview_status=interview_status
    )


# ---------------- ADMIN LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if username == "admin" and password == "admin123":

            session["admin_logged_in"] = True

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


# ---------------- ADMIN DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if not session.get("admin_logged_in"):
        return redirect("/login")

    connection = get_connection()

    candidates = connection.execute("""
        SELECT * FROM candidates
        ORDER BY (score + interview_score) DESC
    """).fetchall()

    total_candidates = connection.execute("""
        SELECT COUNT(*) FROM candidates
    """).fetchone()[0]

    selected = connection.execute("""
        SELECT COUNT(*) FROM candidates
        WHERE selection_status = 'Selected'
    """).fetchone()[0]

    rejected = connection.execute("""
        SELECT COUNT(*) FROM candidates
        WHERE selection_status = 'Rejected'
    """).fetchone()[0]

    under_review = connection.execute("""
        SELECT COUNT(*) FROM candidates
        WHERE selection_status = 'Under Review'
    """).fetchone()[0]

    connection.close()

    return render_template(
        "dashboard.html",
        candidates=candidates,
        total_candidates=total_candidates,
        selected=selected,
        rejected=rejected,
        under_review=under_review
    )

# ---------------- UPDATE SELECTION STATUS ----------------

@app.route("/update_status/<int:candidate_id>", methods=["POST"])
def update_status(candidate_id):

    if not session.get("admin_logged_in"):
        return redirect("/login")

    selection_status = request.form["selection_status"]

    connection = get_connection()

    connection.execute("""
        UPDATE candidates
        SET selection_status = ?
        WHERE id = ?
    """, (
        selection_status,
        candidate_id
    ))

    connection.commit()
    connection.close()

    return redirect("/dashboard")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.pop("admin_logged_in", None)

    return redirect("/login")


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)