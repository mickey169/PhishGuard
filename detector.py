
import re

def analyze_email(email_text):
    text = email_text.lower()

    score = 0
    findings = []

    # Check for urgent language
    urgent_words = [
        "urgent", "immediately", "act now",
        "account suspended", "limited time"
    ]

    for word in urgent_words:
        if word in text:
            score += 15
            findings.append(f"Urgent language detected: '{word}'")

    # Check for requests for sensitive information
    sensitive_words = [
        "password", "otp", "bank details",
        "credit card", "login credentials"
    ]

    for word in sensitive_words:
        if word in text:
            score += 20
            findings.append(f"Sensitive information request indicator: '{word}'")

    # Check for suspicious link patterns
    urls = re.findall(r"https?://[^\s]+|www\.[^\s]+", text)

    if urls:
        score += 15
        findings.append("Email contains one or more links. Check their destinations carefully.")

    # Check for suspicious phrases
    suspicious_phrases = [
        "verify your account",
        "claim your prize",
        "click here",
        "unusual activity"
    ]

    for phrase in suspicious_phrases:
        if phrase in text:
            score += 15
            findings.append(f"Suspicious phrase detected: '{phrase}'")

    # Keep score within 0-100
    score = min(score, 100)

    if score >= 50:
        risk = "High Risk"
    elif score >= 20:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    if not findings:
        findings.append("No indicators from the current rule set were detected.")

    return {
        "score": score,
        "risk": risk,
        "findings": findings
    }
