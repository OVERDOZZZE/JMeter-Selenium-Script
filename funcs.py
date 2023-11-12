import git
import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 100)


def write_down(code, filename):
    with open(filename, "w") as file:
        file.write(code)


def push_to_github(repository_path, file_path, commit_message, remote_name='origin', branch_name='main'):
    repo = git.Repo(repository_path)
    repo.index.add([file_path])
    repo.index.commit(commit_message)
    remote = repo.remote(name=remote_name)
    remote.push(branch_name)


def leetcode_login(login, password):
    driver.get("https://leetcode.com/accounts/login/")
    driver.implicitly_wait(5)

    login_field = driver.find_element(By.ID, 'id_login')
    login_field.send_keys(login)

    password_field = driver.find_element(By.ID, 'id_password')
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, 'signin_btn')
    login_button.click()
    wait.until(EC.url_matches("https://leetcode.com/"))


def get_leetcode_solution(day):
    driver.get('https://leetcode.com/problemset/all/?difficulty=EASY&page=1')
    time.sleep(2)

    problem_list = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]//a[contains(@class, "hover:text-blue-s") and contains(@href, "/problems/") and contains(@class, "dark:hover:text-dark-blue-s")]')
    # problem_list = driver.find_elements(By.XPATH, "//div[@role='rowgroup']//div[@role='cell']//a")
    problem_list[day].click()
    time.sleep(5)

    button = driver.find_element(By.XPATH, f"//span[contains(text(), '{'Solutions'}')]/..")
    button.click()
    time.sleep(5)

    solutions = driver.find_elements(By.XPATH, '//div[@class="group flex w-full cursor-pointer flex-col gap-1.5 px-4 pt-3"]')
    solutions[1].click()
    time.sleep(5)
    code = driver.find_elements(By.CSS_SELECTOR, 'code.language-cpp')

    return code


def publish_story(login, password):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    login_field = driver.find_element(By.NAME, 'username')
    login_field.send_keys(login)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    button = driver.find_element(By.CLASS_NAME, '_acan._acap._acas._aj1-._ap30')
    button.click()

    # wait.until(EC.url_matches('https:/instagram.com/134'))


def fun():
    # driver.get('https://leetcode.com')
    driver.maximize_window()    
    time.sleep(10)
    b1 = driver.find_element(By.CLASS_NAME, "x1i10hfl")
    b1.click()
    time.sleep(5)

    not_now_button = driver.find_element(By.CLASS_NAME, "_a9_1")
    not_now_button.click()

    time.sleep(5)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('i')

    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('m')

    time.sleep(2)
    driver.refresh()
    time.sleep(5)   

    wait.until(EC.url_matches('https:/instagram.com/134'))


if __name__ == '__main__':
    fun()
