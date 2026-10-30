
import sqlite3
from datetime import datetime

DATABASE_NAME = "phishguard.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_type TEXT NOT NULL,
            input_text TEXT NOT NULL,
            risk_level TEXT NOT NULL,
            score INTEGER NOT NULL,
            findings TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_scan(scan_type, input_text, result):
    connection = get_connection()

    connection.execute("""
        INSERT INTO scan_history
        (scan_type, input_text, risk_level, score, findings, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        scan_type,
        input_text,
        result["risk"],
        result["score"],
        "; ".join(result["findings"]),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_history():
    connection = get_connection()

    records = connection.execute("""
        SELECT * FROM scan_history
        ORDER BY id DESC
    """).fetchall()

    connection.close()
    return records

def get_statistics():
    connection = get_connection()

    total_scans = connection.execute(
        "SELECT COUNT(*) FROM scan_history"
    ).fetchone()[0]

    email_scans = connection.execute(
        "SELECT COUNT(*) FROM scan_history WHERE scan_type = 'Email'"
    ).fetchone()[0]

    url_scans = connection.execute(
        "SELECT COUNT(*) FROM scan_history WHERE scan_type = 'URL'"
    ).fetchone()[0]

    high_risk_scans = connection.execute(
        "SELECT COUNT(*) FROM scan_history WHERE risk_level = 'High'"
    ).fetchone()[0]

    connection.close()

    return {
        "total_scans": total_scans,
        "email_scans": email_scans,
        "url_scans": url_scans,
        "high_risk_scans": high_risk_scans
    }