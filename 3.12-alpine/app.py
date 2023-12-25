from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    """ This is just a simple test that creates a driver, fetch a simple page and check that content could be read """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://httpbin.org/html')

    h1 = driver.find_element(by=By.TAG_NAME, value='h1')
    inner_text = h1.text

    driver.quit()

    if inner_text == 'Herman Melville - Moby-Dick':
        return 'OK', 200
    else:
        return 'Not Acceptable', 406 


