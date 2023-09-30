#!/bin/python


from git import Repo, GitCommandError    
from datetime import date
import datetime



# Create a variable for the current date
current_date = date.today()

# Get current time
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()

# Path to local repository
repo_path = '/home/sasha/03.Git/repo/'


# Repository object initialization
repo = Repo(repo_path)


# Getting a list of deleted repositories
remote_repositories = repo.remotes


# Generating a list of URLs of remote repositories
remote_urls = [remote.url for remote in remote_repositories]


# Creating a remote repository object for each URL
#remote_repos = [repo.create_remote(name=str(i), url=url) for i, url in enumerate(remote_urls)]
try:
    remote_repos = []
    for i, url in enumerate(remote_urls):
        try:
            remote_repos.append(repo.create_remote(name=str(i), url=url))
        except GitCommandError as e:
            if "remote {} already exists".format(i) in str(e):
                pass
                # Обработка ошибки, если удаленный репозиторий уже существует
                #remote_repos.append(repo.remotes[str(i)])
            else:
                # Обработка других ошибок
                raise e
except Exception as e:
    # Обработка любых других исключений
    print("Произошла ошибка:", str(e))
print(remote_repos)


# Uploading all changes to the local repository
repo.git.add('--all')
print('Git add OK!')

# Fixing changes
dt = f"Date:   {current_date}  Time:  {current_time}"
repo.git.commit('-m', dt)
print('Commit OK!')

# Send changes to all remote repositories
for remote_repo in remote_repos:
    remote_repo.push()
print('Push OK!')

