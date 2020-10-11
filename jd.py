from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import datetime

snap_up_time = "2020-10-10-10-00"
shop_id = "100008461335"

class pay_text_present(object):
  def __init__(self, locator, type_value):
    self.locator = locator
    self.type_value = type_value

  def __call__(self, driver):
    #print(time.time())
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.type_value == element.text:
      return element
    else:
      return False
class pay_present(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, type_value):
    self.locator = locator
    self.type_value = type_value

  def __call__(self, driver):
    #print(time.time())
    elements = driver.find_elements(*self.locator)   # Finding the referenced element
    for elm in elements:
        print(elm.text)
        if self.type_value == elm.text:
            return elm
    return False

# 计算等待时间
strg = snap_up_time
dt = datetime.datetime.strptime(strg, '%Y-%m-%d-%H-%M')
tme = dt.timestamp()


# 加入购物车
browser = webdriver.Chrome()
browser.get('https://p.m.jd.com/norder/order.action?wareNum=1&wareId=' + shop_id)

wait = WebDriverWait(browser, 3600, 0.001)
#element = wait.until(pay_present((By.CSS_SELECTOR, 'div.pay_area.new>div>div.mod_btns_v2:not([style])>a.mod_btn.bg_2'), '在线支付'))
element = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "在线支付")))
#time.sleep(5)
#element.click()
#browser.execute_script("arguments[0].click();", element)



# 等待
now = datetime.datetime.now().timestamp()
wait_time = tme - now - 1
if wait_time > 0:
    print('waiting ' + wait_time.__str__() + 's')
    time.sleep(wait_time)


while True:
    now = datetime.datetime.now().timestamp()
    #print('polling... ' + now.__str__())
    if now >= tme:
        break

# 抢购
element.click()
