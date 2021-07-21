from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)   
    #time.sleep(10)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    
    
    # Вводим ответ в текстовое поле
    input1 = browser.find_element_by_css_selector("div.container div #answer")
    input1.send_keys(y)
    
        
    # Отправляем ответ
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()