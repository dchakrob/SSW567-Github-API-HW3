''' 
Name: Danica Chakroborty
Assignment: GithubAPI
Github Link: 
I pledge my honor that I have abided by the Stevens Honor System - Danica Chakroborty
'''

import requests
import json

def get_github_repos(user_id):
    url = "https://api.github.com/users/" + user_id + "/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = json.loads(response.text)
        repo_names = []
        for repo in repos:
            repo_name = repo["name"]
            repo_names.append(repo_name)
        return repo_names
    else:
        return None

def get_commits(user_id, repo_name):
    url = "https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = json.loads(response.text)
        return len(commits)
    else:
        return None

def github_info(user_id):
    repos = get_github_repos(user_id)

    if repos is None:
        return None

    results = []

    for repo_name in repos:
        commits = get_commits(user_id, repo_name)
        results.append((repo_name, commits))

    return results

if __name__ == "__main__":
    results = github_info("richkempinski")

    if results is not None:
        for repo_name, commits in results:
            print(f"Repo: {repo_name} Number of commits: {commits}")




