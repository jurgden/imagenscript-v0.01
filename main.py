from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 



def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=options)
  driver.get('https://titan22.com/account/login?return_url=%2Faccount')
  return driver 


def main():
  driver = get_driver()
  driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[1]/input').send_keys('eopimboaobdo@dropmail.me')
  time.sleep(2)
  driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[2]/input').send_keys('xboxlive3' + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by='xpath', value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  print(driver.current_url)
  time.sleep(2)
  return print(driver.current_url)

print(main())