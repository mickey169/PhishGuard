# PhishGuard – Phishing Attack Simulation and Detection System

PhishGuard is a student cybersecurity project developed to demonstrate basic phishing detection techniques and improve awareness of phishing attacks.

The application provides tools to analyze suspicious email content and URLs, practice phishing awareness through quizzes and educational simulations, and maintain a history of scan results.

## Features

- **Email Phishing Detector:** Analyzes email content for suspicious words and phishing indicators.
- **URL Scanner:** Checks URLs for potentially suspicious characteristics.
- **Dashboard:** Displays statistics about email scans, URL scans, and high-risk results.
- **Phishing Awareness Quiz:** Tests users' knowledge of phishing attacks.
- **Educational Simulation:** Uses fictional examples to demonstrate common phishing warning signs.
- **Scan History:** Stores previous scan results using SQLite.
- **CSV Export:** Allows users to download scan history as a CSV report.
- **About Page:** Explains the project's objectives and technologies.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- SQLite
- Pandas
- Scikit-learn

## Project Structure

```text
PhishGuard/
│
├── app.py
├── detector.py
├── url_detector.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── email_detector.html
│   ├── url_scanner.html
│   ├── quiz.html
│   ├── simulation.html
│   ├── history.html
│   └── about.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/PhishGuard.git
cd PhishGuard
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open PhishGuard

Visit this address in your browser:

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user submits email content or a URL for analysis.
2. PhishGuard checks the submitted input using its detection logic.
3. The application displays a risk assessment and findings.
4. Scan results are stored in the local SQLite database.
5. Users can view their scan history and export reports as CSV.

## Project Objectives

- Understand common phishing attack techniques.
- Demonstrate basic phishing detection methods.
- Improve cybersecurity awareness.
- Practice Python web development and database integration.
- Build a practical cybersecurity project.

## Limitations

PhishGuard is an educational demonstration project. Its rule-based detection methods may produce false positives or miss sophisticated phishing attacks. It does not guarantee that a URL or email is safe.

The project does not open submitted URLs or collect real credentials, passwords, or OTPs.

## Future Improvements

- Integrate a properly evaluated machine-learning phishing classifier.
- Improve URL and email analysis techniques.
- Add more awareness questions and educational examples.
- Improve reporting and visualization features.

## Disclaimer

This project is developed for educational and cybersecurity awareness purposes only. The simulation uses fictional examples and is not intended to conduct real phishing attacks.

## Author

Developed as a student cybersecurity internship project.

**Project Name:** PhishGuard  
**Category:** Cybersecurity / Phishing Detection
