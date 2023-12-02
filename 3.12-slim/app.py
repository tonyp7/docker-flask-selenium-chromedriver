from flask import Flask, Response
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    """ This is just a simple test that creates a driver, fetch google.com and return the page source as plain text """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    driver.get('https://www.google.com/')

    source = driver.page_source
    driver.quit()

    response = Response(source, status=200, mimetype='text/plain')
    return response


