#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import signal, os, math, sys
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

BASE_URL="https://www.cvedetails.com/"
LINUX_CVES="https://www.cvedetails.com/vulnerability-list/vendor_id-33/product_id-47/Linux-Linux-Kernel.html?page={}&year={}&order=1"

def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    driver.close()
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

# Accept cookies consent
def accept_consent(driver):
    element = driver.find_element(By.LINK_TEXT, "Close")
    element.click()

driver = webdriver.Firefox()

def get_cves_list(driver, year):
    url = LINUX_CVES.format(1, year)
    print(url)
    driver.get(url)
    accept_consent(driver)
    elements = driver.find_elements(By.XPATH, "//div[@class='flex-grow-1 paging']")
    for e in elements:
        inner_html = e.get_attribute('innerHTML')
        soup = BeautifulSoup(inner_html)
        links = soup.find_all("a")
        inner_html = links[1:]
    return inner_html

def get_csv_data(driver, url_list, f):
    for page, url in zip(range(1, len(url_list) + 1), url_list):
        driver.get(url)
        # Copy the csv of this page
        element = driver.find_element(By.LINK_TEXT, "Copy")
        # now the CSV is copied to clipboard
        element.click()
        # paste from clipboard and write to file
        if page > 1:
            cve_list = pyperclip.paste().split('\n')[1:]
            cve_data = "\n".join(cve_list)
        else:
            cve_data = pyperclip.paste()
        f.write(cve_data)
    f.close()

for year in range(2014, 2023 + 1):
    f = open("linux-cves-" + str(year) + ".csv", "a")
    driver.get(LINUX_CVES.format("1", year))
    accept_consent(driver)
    element = driver.find_element(By.XPATH, "//div[@class='ssc-text-secondary mb-2']")
    num_vulns = element.text.split(' ')[0]
    num_pages = math.ceil(int(num_vulns) / 25)
    print("Year: {} , num CVEs = {}".format(year, num_vulns))
    num_pages = 1
    a_tags = get_cves_list(driver, year)
    url_list = []
    for tag in a_tags:
        href = tag['href']
        print(href)
        url_list.append(BASE_URL + href)

    get_csv_data(driver, url_list, f)

driver.close()
