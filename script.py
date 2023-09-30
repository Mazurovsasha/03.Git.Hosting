#!/bin/python


from git import Repo     


# Path to local repository
repo_path = '/home/sasha/03.Git/repo/'


# Repository object initialization
repo = Repo(repo_path)


# Getting a list of deleted repositories
remote_repositories = repo.remotes


# Generating a list of URLs of remote repositories
remote_urls = [remote.url for remote in remote_repositories]


# Creating a remote repository object for each URL
remote_repos = [repo.create_remote(name=str(i), url=url) for i, url in enumerate(remote_urls)]


# Uploading all changes to the local repository
repo.git.add('--all')
print('Git add OK!')

# Fixing changes
repo.git.commit('-m', 'Автоматический коммит')
print('Commit OK!')

# Send changes to all remote repositories
for remote_repo in remote_repos:
    remote_repo.push()
print('Push OK!')

