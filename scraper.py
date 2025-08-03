import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_court_data(case_type, case_number, filing_year):
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Case Status"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "case_type"))
        )
        driver.find_element(By.NAME, "case_type").send_keys(case_type)
        driver.find_element(By.NAME, "case_number").send_keys(case_number)
        driver.find_element(By.NAME, "case_year").send_keys(filing_year)

        driver.find_element(By.ID, "searchbtn").click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "case_details_table"))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        party_td = soup.find("td", text="Petitioner")
        filing_td = soup.find("td", text="Filing Date")
        hearing_td = soup.find("td", text="Next Hearing Date")

        data = {
            "party_names": party_td.find_next_sibling("td").get_text(strip=True) if party_td else "N/A",
            "filing_date": filing_td.find_next_sibling("td").get_text(strip=True) if filing_td else "N/A",
            "next_hearing": hearing_td.find_next_sibling("td").get_text(strip=True) if hearing_td else "N/A",
            "order_link": None
        }

        link = soup.find("a", href=True, text=lambda t: "Order" in t or "Judgment" in t)
        if link:
            data["order_link"] = link['href']

        driver.quit()
        return data, None

    except Exception as e:
        try:
            driver.quit()
        except:
            pass
        return None, f"Error fetching data: {str(e)}"
