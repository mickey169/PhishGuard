import csv
import io

from database import init_db, save_scan, get_history, get_statistics
init_db()

from flask import Flask, render_template, request, Response

from detector import analyze_email
from url_detector import analyze_url

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    stats = get_statistics()
    return render_template("index.html", stats=stats)


# Email phishing detector
@app.route("/email-detector", methods=["GET", "POST"])
def email_detector():
    result = None
    email_text = ""

    if request.method == "POST":
        email_text = request.form.get("email_text", "").strip()

        if email_text:
            result = analyze_email(email_text)
            save_scan("email", email_text, result)

    return render_template(
        "email_detector.html",
        result=result,
        email_text=email_text
    )


# URL phishing scanner
@app.route("/url-scanner", methods=["GET", "POST"])
def url_scanner():
    result = None
    submitted_url = ""

    if request.method == "POST":
        submitted_url = request.form.get("url", "").strip()

        if submitted_url:
            result = analyze_url(submitted_url)
            save_scan("url", submitted_url, result)

    return render_template(
        "url_scanner.html",
        result=result,
        submitted_url=submitted_url
    )


@app.route("/simulation")
def simulation():
    return render_template("simulation.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/history")
def history():
    records = get_history()
    return render_template("history.html", records=records)


@app.route("/export")
def export_history():
    records = get_history()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Scan Type",
        "Input",
        "Risk Level",
        "Score",
        "Findings",
        "Date"
    ])

    for record in records:
        writer.writerow([
            record["id"],
            record["scan_type"],
            record["input_text"],
            record["risk_level"],
            record["score"],
            record["findings"],
            record["created_at"]
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=phishguard_report.csv"
        }
    )

@app.route("/about")
def about():
    return render_template("about.html")
    
# Start application
if __name__ == "__main__":
    app.run(debug=True)
