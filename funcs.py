import os.path
import git
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(options=options)
browser = options.capabilities["browserName"]
wait = WebDriverWait(driver, 10)


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
    driver.maximize_window()
    time.sleep(4)

    problem_list = wait.until(EC.visibility_of_all_elements_located((
        By.XPATH, '//div[@role="rowgroup"]//a[contains(@class, "hover:text-blue-s") and contains(@href, "/problems/") and contains(@class, "dark:hover:text-dark-blue-s")]'))
    )
    problem_list[day].click()

    button = wait.until(EC.visibility_of_element_located((
        By.XPATH, f"//span[contains(text(), '{'Solutions'}')]/.."))
    )
    button.click()

    solutions = wait.until(EC.visibility_of_all_elements_located((
        By.XPATH, '//div[@class="group flex w-full cursor-pointer flex-col gap-1.5 px-4 pt-3"]'))
    )
    solutions[1].click()

    code = wait.until(EC.visibility_of_all_elements_located((
        By.XPATH, "//*[starts-with(@class, 'language-')]"))
    )
    return code


def take_screenshot(link, day, screens_path):
    driver.get(link)
    driver.maximize_window()
    image_path = os.path.join(screens_path, f'image{day}.png')
    driver.save_screenshot(
        image_path
        # f'C:\\Users\\User\\PycharmProjects\\Selenim-Jmet\\Selenium-JMeter\\screens\\image{day}.png'
    )
    image = Image.open(image_path)
    width, height = image.size
    cropped_image = image.crop((0, 0, width//4, height))
    cropped_image.save(image_path)
    driver.quit()
