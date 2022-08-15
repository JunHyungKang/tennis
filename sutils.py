from selenium import webdriver

def get_selenium_driver(headless=True):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('lang=en')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver