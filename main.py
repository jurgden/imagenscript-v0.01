from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from rand_select import rand_select
import urllib.request
import datetime as dt
import logger as log

debug = log.logger.debug
info = log.logger.info
warning = log.logger.warning
error = log.logger.error
critical = log.logger.critical


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    driver.get('https://app.baseten.co/apps/VBlnMVP/operator_views/nBrd8zP')
    return driver


###### LISTS ########
list_1 = [
    'shake', 'palace', 'virus', 'domination', 'studio', 'pension', 'snail'
]
list_2 = [
    'sun', 'reject', 'affinity', 'active', 'vibrant', 'high-contrast', 'reptiles'
]
listolist = [list_1, list_2]
####### LISTS ########

intdt = dt.datetime.now()

fname = f'file{intdt}.png'


def main():
  
  driver = get_driver()
  time.sleep(2)
  driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div/input'
    ).send_keys(f'{rand_select(listolist)}')
  time.sleep(1.7)
  driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div[1]/div/div/div/div[5]/div/div/div/div[2]/button/div'
    ).click()
  time.sleep(120)
  try:
      img = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[6]/div/div/div/div[2]/img')
      src = img.get_attribute('src')
      time.sleep(3)
      pic = urllib.request.urlretrieve(src, fname)
      return pic
  except:
      info('Image pulled to early!')
      main()
while True:
  try:
    main()
  except:
    critical('Error with main function call!\nRestarting our loop...')
