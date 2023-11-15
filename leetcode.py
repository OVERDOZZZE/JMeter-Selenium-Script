from funcs import write_down, push_to_github, get_leetcode_solution, take_screenshot
import os
from git import Repo
from datetime import datetime
solution_file_path = './code/solution.cpp'
solution_folder_path = 'code'

solution_file_path_absolute = os.path.abspath(solution_file_path)
solution_folder_path_absolute = os.path.abspath(solution_folder_path)


# LOCAL_REPO = r"C:\Users\User\PycharmProjects\Selenim-Jmet\Selenium-JMeter\hub"
# REMOTE_REPO = "https://github.com/OVERDOZZZE/JMeter-31day/blob/main/hub.cpp"
day = int(datetime.today().day) - 17
# day = 9

if __name__ == '__main__':
    try:
        if not os.path.exists(solution_file_path):
            os.makedirs('./code ', exist_ok=True)

            with open(solution_file_path, 'w'):
                pass
        try:
            repo = Repo(solution_folder_path_absolute)
        except Exception as e:
            repo = Repo.init(solution_folder_path_absolute)
            remote_name = 'origin'
            remote_exists = any(remote.name == remote_name for remote in repo.remotes)
            if not remote_exists:
                remote_url = input('Your remote repository url: ')
                origin = repo.create_remote(remote_name, remote_url)
            else:
                pass

        LOCAL_REPO = solution_folder_path_absolute
        REMOTE_REPO = repo.remote().url

        if day:
            code = get_leetcode_solution(day=day)
            write_down(
                code[0].text, solution_file_path_absolute
            )
            push_to_github(
                repository_path=LOCAL_REPO,
                file_path=solution_file_path_absolute,
                commit_message=f"commit-{day}",
            )

            print('New code has been successfully uploaded to github!')

            take_screenshot(link=REMOTE_REPO, day=day)
            print('New screenshot has been taken!')
            from instagram import login_instagram, publish_story
            login_instagram('a3.djedai', 'nurdan2005.')
            publish_story(day=day)
            print("Story has been published! Today's done!")

    except Exception as e:
        print(e)

