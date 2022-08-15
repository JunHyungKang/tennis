import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

from sutils import get_selenium_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = get_selenium_driver(False)
driver.get('https://www.sujigu.go.kr/lmth/04life06Write_1.asp?sisul_idx=3&sel_dd=2022-08-16&sel_time=12#sin')

id = '아이디 입력'
pw = '비밀번호 입력'

try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'login')))
    elem_btn = driver.find_element(By.CLASS_NAME, 'login')
    elem_btn.click() # 버튼 클릭

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'j_username')))
    elem_id = driver.find_element(By.ID, 'j_username')
    elem_id.send_keys(id) # id 입력

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'j_password')))
    elem_pw = driver.find_element(By.ID, 'j_password')
    elem_pw.send_keys(pw)

    login_btn = driver.find_element(By.XPATH, '//button[@class="button large width-max"]')
    login_btn.click()
except: # 이미 로그인이 되어있는 경우
    pass 