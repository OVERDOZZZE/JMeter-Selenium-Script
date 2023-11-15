from funcs import write_down, push_to_github, get_leetcode_solution, take_screenshot
import os
from git import Repo
from decouple import config
from datetime import datetime


def run(day):
    try:
        if not os.path.exists(solution_folder_path):
            os.makedirs('./code ', exist_ok=True)
            with open(solution_file_path, 'w'):
                pass
        try:
            repo = Repo(solution_folder_path_absolute)
        except:
            repo = Repo.init(solution_folder_path_absolute)
            remote_name = 'origin'
            remote_exists = any(remote.name == remote_name for remote in repo.remotes)
            if not remote_exists:
                remote_url = config('REMOTE_REPO_URL')
                origin = repo.create_remote(remote_name, remote_url)
            else:
                pass

        LOCAL_REPO = solution_folder_path_absolute
        REMOTE_REPO = repo.remote().url

        if day:
            code = get_leetcode_solution(day=day)
            write_down(
                code=code[0].text,
                filename=solution_file_path_absolute
            )
            push_to_github(
                repository_path=LOCAL_REPO,
                file_path=solution_file_path_absolute,
                commit_message=f"commit-{day}",
            )

            print('New code has been successfully uploaded to github!')

            take_screenshot(
                link=REMOTE_REPO,
                day=day,
                screens_path=screens_file_path_absolute
            )
            print('New screenshot has been taken!')

            from instagram import login_instagram, publish_story
            login_instagram(
                login=config('LOGIN'),
                password=config('PASSWORD')
            )
            publish_story(
                day=day,
                screens_path=screens_file_path_absolute
            )
            print("Story has been published! Today's done!")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    DAY = int(datetime.today().day) - 17
    solution_file_path = './code/solution.cpp'
    solution_folder_path = 'code'

    solution_file_path_absolute = os.path.abspath(solution_file_path)
    solution_folder_path_absolute = os.path.abspath(solution_folder_path)

    screens_file_path_absolute = os.path.abspath(f'screens')

    run(day=DAY)
