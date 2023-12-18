import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://altema.jp/dotyusya/hultuki')

element_to_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'dummy'))
)
element_to_click.click()

# テキストフィールドに入力
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'comment_content_add1'))
)
input_field.send_keys('2d79884b6845')

print(input_field.get_attribute('value'))

# 送信ボタンをクリック
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'comment_submit'))
)
driver.execute_script("arguments[0].click();", submit_button)


from selenium.webdriver.common.alert import Alert

WebDriverWait(driver, 10).until(EC.alert_is_present())

# ポップアップにアクセスし、エンターキーを押す
alert = Alert(driver)
alert.accept()  # エンターキーを押すのと同じ（OKをクリック）


import time

time.sleep(60)
# ブラウザを閉じる
driver.close()
