from funcs import write_down, push_to_github, leetcode_copy_code, leetcode_login

DAY = 0
LOCAL_REPO = r"C:\Users\User\PycharmProjects\Selenim-Jmet\Selenium-JMeter\github"
PROBLEM_PATH = 'https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/'


if __name__ == '__main__':
    try:
        leetcode_login('saparbekov113@gmail.com', 'nurdan2005.')
        code = leetcode_copy_code(PROBLEM_PATH)
        write_down(
            code[DAY].text, 'github/hub.cpp'
        )
        push_to_github(
            repository_path = LOCAL_REPO,
            file_path = "hub.cpp",
            commit_message = f"commit-{DAY}",
        )
        print(len(code))
        print('Success!')
    except Exception as e:
        print(e)
        