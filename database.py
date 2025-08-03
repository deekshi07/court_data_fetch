import sqlite3

DB_FILE = 'court_queries.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            party_names TEXT,
            filing_date TEXT,
            next_hearing TEXT,
            order_link TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(case_type, case_number, filing_year, data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, party_names, filing_date, next_hearing, order_link)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        case_type, case_number, filing_year,
        data.get('party_names'),
        data.get('filing_date'),
        data.get('next_hearing'),
        data.get('order_link')
    ))
    conn.commit()
    conn.close()
