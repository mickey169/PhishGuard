
from urllib.parse import urlparse
import ipaddress
import re

def analyze_url(url):
    url = url.strip()

    # Add a scheme if the user did not provide one
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.hostname or ""

    score = 0
    findings = []

    # Check whether HTTPS is used
    if parsed.scheme != "https":
        score += 15
        findings.append("URL does not use HTTPS encryption.")

    # Check for an IP address instead of a domain
    try:
        ipaddress.ip_address(domain)
        score += 30
        findings.append("URL uses an IP address instead of a domain name.")
    except ValueError:
        pass

    # Check for URL shortening services
    shorteners = [
        "bit.ly", "tinyurl.com", "t.co",
        "is.gd", "cutt.ly"
    ]

    if domain.lower() in shorteners:
        score += 25
        findings.append("URL uses a shortening service that hides its final destination.")

    # Check for suspicious words in the URL
    suspicious_words = [
        "login", "verify", "account",
        "password", "update", "secure"
    ]

    url_lower = url.lower()

    for word in suspicious_words:
        if word in url_lower:
            score += 10
            findings.append(f"Suspicious keyword found in URL: '{word}'")

    # Check for unusually long URLs
    if len(url) > 100:
        score += 15
        findings.append("URL is unusually long.")

    # Check for excessive subdomains
    if len(domain.split(".")) > 4:
        score += 15
        findings.append("URL contains an unusually large number of domain sections.")

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
