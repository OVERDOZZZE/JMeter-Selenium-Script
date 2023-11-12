import git
import time
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
    problem_list = driver.find_elements(By.XPATH, "//div[@role='rowgroup']//div[@role='cell']//a")
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

