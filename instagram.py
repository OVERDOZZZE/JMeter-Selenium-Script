import os.path
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0 },
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X)"
                    " AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75"
                    " Mobile Safari/535.19"
    }


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--auto-open-devtools-for-tabs')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


def login_instagram(login, password):
    driver.get('https://www.instagram.com/')
    login_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Войти')]")
        )
    )
    login_button.click()
    
    login_field = driver.find_element(By.NAME, 'username')
    login_field.send_keys(login)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Войти')]")
        )
    )
    button.click()


def publish_story(day, screens_path):
    driver.maximize_window()
    decline_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Не сейчас')]")
        )
    )
    decline_button.click()

    time.sleep(5)
    keyboard.press('ctrl')
    keyboard.press('shift')
    keyboard.press('m')
    keyboard.release('ctrl')
    keyboard.release('shift')
    keyboard.release('m')
    time.sleep(2)
    add_element_xpath = "//div[@class='x78zum5 xl56j7k']//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']"
    press_add_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, add_element_xpath)
        )
    )
    press_add_element.click()

    add_story_button_xpath = '//*[@class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft" and text()="История"]'
    press_add_story = wait.until(EC.visibility_of_element_located(
        (By.XPATH, add_story_button_xpath)
        )
    )
    press_add_story.click()
    time.sleep(1)
    controller = Controller()
    controller.type(os.path.join(
        screens_path,
        f'image{day}.png')
    )
    controller.press(Key.enter)
    controller.release(Key.enter)

    add_text_button = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, '_aa3j._9_20')
        )
    )
    add_text_button.click()
    time.sleep(2)
    add_text = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, '_aa77')
        )
    )
    add_text.send_keys('@lazyxnasty')
    touch_men = wait.until(EC.visibility_of_element_located(
        (By.ID, 'touch_mention')
        )
    )
    touch_men.click()
    time.sleep(2)
    try:
        submit_text_button = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, '_aa76')
            )
        )
        submit_text_button.click()
    except Exception as e:
        print(e)

    final_button = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, '_aa33')
        )
    )
    final_button.click()

    WebDriverWait(driver, 10).until(EC.url_matches('https://www.instagram.com/123'))
