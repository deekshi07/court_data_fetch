# ⚖️ Court Data Fetcher & Analytics Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" />
</p>

An automated web application and legal data extraction pipeline designed to query Indian District Court services (eCourts), scrape real-time case status and hearing records, and persist query history into a local SQLite datastore with interactive dashboard visualization.

---

## 📌 Key Capabilities

- **Automated Case Lookup:** Queries eCourts portal via Case Type, Case Number, and Filing Year.
- **Headless Browser Orchestration:** Leverages Selenium WebDriver to handle dynamic DOM updates, iframes, and session-based page loads.
- **Data Extraction:** Extracts party names, case filing date, next hearing date, and direct PDF links for judgment/order downloads.
- **Persistent Storage:** Caches all queries in a local SQLite database (`court_queries.db`) to enable instant search history without repetitive scraping.
- **Interactive Web UI:** Clean Flask-rendered dashboard for submitting lookups and reviewing structured case timelines.

---

## 🏗️ Architecture & Workflow

```
┌─────────────────┐       POST /fetch       ┌────────────────────────┐
│                 ├────────────────────────►│                        │
│   Web Browser   │                         │     Flask App Server   │
│  (UI Dashboard) │◄────────────────────────┤       (app.py)         │
└─────────────────┘       HTML Results      └───────────┬────────────┘
                                                        │
                         ┌──────────────────────────────┴──────────────────────────────┐
                         ▼                                                             ▼
             ┌─────────────────────────┐                                   ┌───────────────────────┐
             │    Selenium Driver      │                                   │   SQLite Database     │
             │   eCourts Web Scraper   │                                   │  (court_queries.db)   │
             └───────────┬─────────────┘                                   └───────────────────────┘
                         │
                         ▼
             ┌─────────────────────────┐
             │  services.ecourts.gov.in│
             │   District Court Portal │
             └─────────────────────────┘
```

---

## 📂 Project Structure

```text
court_data_fetch/
├── app.py              # Flask server and web routes
├── scraper.py          # Selenium web scraping logic and DOM selectors
├── database.py         # SQLite connection and query persistence layer
├── court_queries.db    # SQLite database file
├── requirements.txt    # Python dependencies
├── static/             # CSS styling and static assets
└── templates/          # HTML templates (index.html, results.html)
```

---

## ⚡ Quickstart Guide

### 1. Prerequisites
- Python 3.9+ installed
- Google Chrome browser installed (compatible with Chrome WebDriver)

### 2. Installation & Setup

```bash
# Clone the repository
git clone https://github.com/deekshi07/court_data_fetch.git
cd court_data_fetch

# Create and activate virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000` to access the case lookup interface.

---

## 🛡️ Limitations & Disclaimer

- The scraper interacts with the live eCourts portal interface; changes to third-party DOM hierarchy or CAPTCHA enforcement may require updating selector configurations.
- Intended strictly for educational, research, and non-commercial automation testing purposes.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
