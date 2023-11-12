import git
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()


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
    wait = WebDriverWait(driver, 100)
    wait.until(EC.url_matches("https://leetcode.com/"))
    

def leetcode_copy_code(problem):    
    driver.get(problem)
    code = driver.find_elements(By.CSS_SELECTOR, 'code.language-cpp')

    return code
