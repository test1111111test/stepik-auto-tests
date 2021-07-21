from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button1 = browser.find_element_by_id("book")
    button1.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
        
    # Вводим ответ в текстовое поле
    input1 = browser.find_element_by_css_selector("div.container div #answer")
    input1.send_keys(y)
    
        
    # Отправляем ответ
    button = browser.find_element_by_id("solve")
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()