from funcs import write_down, push_to_github, get_leetcode_solution

DAY = 4
LOCAL_REPO = r"C:\Users\User\PycharmProjects\Selenim-Jmet\Selenium-JMeter\hub"
PROBLEM_PATH = 'https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/'


if __name__ == '__main__':
    try:
        code = get_leetcode_solution(day=DAY)
        write_down(
            code[0].text, 'hub/hub.cpp'
        )
        push_to_github(
            repository_path = LOCAL_REPO,
            file_path = "hub.cpp",
            commit_message = f"commit-{DAY}",
        )
        print('Success!')
    except Exception as e:
        print(e)
        