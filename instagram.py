import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19" }


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--auto-open-devtools-for-tabs')
chrome_options.add_argument('--remote-debugging-port=9222')  # Добавьте эту опцию
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 100)


def login_instagram(login, password):
    driver.get('https://www.instagram.com/')
    login_button = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Войти')]"))
    )
    login_button.click()
    
    login_field = driver.find_element(By.NAME, 'username')
    login_field.send_keys(login)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Войти')]"))
    )
    button.click()


def publish_story(day):  
    driver.maximize_window()
    decline_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Не сейчас')]"))
    )
    decline_button.click()

    time.sleep(5)
    keyboard.press('ctrl')
    keyboard.press('shift')
    keyboard.press('m')
    keyboard.release('ctrl')
    keyboard.release('shift')
    keyboard.release('m')
    time.sleep(5)

    publish_story_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, '_aac0'))
    )
    publish_story_button.click()

    # publish_element_button = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, 'form:nth-of-type(2) input._ac69'))
    # )
    # print('pass 2')
    # # publish_element_button.click()
    # print('pass 3')
    #
    # publish_story_button = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "//span[contains(text(),'История')]"))
    # )
    # publish_story_button.click()

    time.sleep(2)
    controller = Controller()
    controller.type(f"C:\\Users\\User\\PycharmProjects\\Selenim-Jmet\\Selenium-JMeter\\screens\\image{day}.png") 
    controller.press(Key.enter)
    controller.release(Key.enter)

    final_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_aa33')))
    final_button.click()

    wait.until(EC.url_matches('https://www.instagram.com/'))


if __name__ == '__main__':
    login_instagram('a3.djedai', 'nurdan2005.')
    publish_story(1)
