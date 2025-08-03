<<<<<<< HEAD
# court_data_fetch
court_data_fetch
=======
# --------------------------
# README.md (Content Outline)
# --------------------------
# Court-Data Fetcher & Mini-Dashboard

## 🔎 Court Targeted
Faridabad District Court (https://districts.ecourts.gov.in/faridabad)

## 📋 Features
- User inputs: Case Type, Number, Year
- Scrapes case metadata & judgment links
- Stores all queries in SQLite
- Displays results in browser
- PDF download supported

## ⚙️ Technologies
- Flask, SQLite, BeautifulSoup, Requests

## 🧩 CAPTCHA Handling
No CAPTCHA required for basic queries.

## 🚀 Running Instructions
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 🐛 Limitations
- May break if court HTML structure changes
- CAPTCHA may block automation on other courts
>>>>>>> ad32579 (initial)
