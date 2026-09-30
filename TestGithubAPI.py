
''' 
Name: Danica Chakroborty
Assignment: GithubAPI
Github Link: https://github.com/dchakrob/SSW567-Github-API-HW3/blob/main/TestGithubAPI
I pledge my honor that I have abided by the Stevens Honor System - Danica Chakroborty
'''
import unittest

from GithubAPI import get_github_repos, get_commits, github_info


class TestGithubAPI(unittest.TestCase):

    def test_get_github_repos(self):
        repos = get_github_repos("richkempinski")
        self.assertIsNotNone(repos)
        self.assertIsInstance(repos, list)
        self.assertIn("hellogitworld", repos)

    def test_get_commits(self):
        commits_count = get_commits("richkempinski", "hellogitworld")
        self.assertIsNotNone(commits_count)
        self.assertIsInstance(commits_count, int)

    def test_github_info(self):
        results = github_info("richkempinski")

        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)

        repo_names = []

        for repo_name, commits in results:
            repo_names.append(repo_name)
            self.assertIsInstance(commits, int)

        self.assertIn("hellogitworld", repo_names)

    def test_invalid_user(self):
        repos = get_github_repos("thisuserdoesnotexist123456789")
        self.assertIsNone(repos)


if __name__ == "__main__":
    unittest.main()
