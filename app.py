from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    data = scrape_court_data(case_type, case_number, filing_year)
    return render_template('results.html', data=data)

def scrape_court_data(case_type, case_number, filing_year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/"
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Click District Court Services
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "District Court Services"))).click()
        
        # Switch to iframe
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "contentAreaFrame")))

        # Click on Case Status
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "casestatus"))).click()

        # Fill in form
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cino"))).send_keys("DHC010003012023")

        # Click Submit
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

        time.sleep(3)  # Allow page to update

        # Scrape example info (update selectors based on actual site)
        parties = driver.find_element(By.ID, "partyName").text
        filing_date = driver.find_element(By.ID, "fdate").text
        next_hearing = driver.find_element(By.ID, "nxd").text
        order_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Order").get_attribute('href')

        driver.quit()

        return {
            'party_names': parties,
            'filing_date': filing_date,
            'next_hearing': next_hearing,
            'order_link': order_link
        }

    except Exception as e:
        driver.quit()
        print(f"Error: {e}")
        return {
            'party_names': 'Unavailable',
            'filing_date': 'Unavailable',
            'next_hearing': 'Unavailable',
            'order_link': '#'
        }

if __name__ == '__main__':
    app.run(debug=True)
