from funcs import write_down, push_to_github, get_leetcode_solution, take_screenshot
from instagram import login_instagram, publish_story

LOCAL_REPO = r"C:\Users\User\PycharmProjects\Selenim-Jmet\Selenium-JMeter\hub"
REMOTE_REPO = "https://github.com/OVERDOZZZE/JMeter-31day/blob/main/hub.cpp"
PROBLEM_PATH = 'https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/'
day = int(input('Choose day (from 1 to 31): '))

if __name__ == '__main__':
    try:
        if day:
            code = get_leetcode_solution(day=day)
            write_down(
                code[0].text, 'hub/hub.cpp'
            )
            push_to_github(
                repository_path=LOCAL_REPO,
                file_path="hub.cpp",
                commit_message=f"commit-{day}",
            )

            print('New code had been successfully uploaded to github!')

            take_screenshot(link=REMOTE_REPO, day=day)
            
            login_instagram('a3.djedai', 'nurdan2005.')
            publish_story(day=day)
            print("Story had been published! Today's done!")

    except Exception as e:
        print(e)
        