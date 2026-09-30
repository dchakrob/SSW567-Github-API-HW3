'''
Name: Danica Chakroborty
Assignment: GithubAPI
Github Link: https://github.com/dchakrob/SSW567-Github-API-HW3
I pledge my honor that I have abided by the Stevens Honor System - Danica Chakroborty
'''

import unittest
from unittest.mock import patch, Mock

from GithubAPI import get_github_repos, get_commits, github_info


class TestGithubAPI(unittest.TestCase):

    @patch("GithubAPI.requests.get")
    def test_get_github_repos(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '[{"name": "hellogitworld"}, {"name": "Mocks"}]'
        mock_get.return_value = mock_response

        repos = get_github_repos("richkempinski")

        self.assertIsNotNone(repos)
        self.assertIsInstance(repos, list)
        self.assertIn("hellogitworld", repos)

    @patch("GithubAPI.requests.get")
    def test_get_commits(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '[{"sha": "123"}, {"sha": "456"}, {"sha": "789"}]'
        mock_get.return_value = mock_response

        commits_count = get_commits("richkempinski", "hellogitworld")

        self.assertIsNotNone(commits_count)
        self.assertIsInstance(commits_count, int)
        self.assertEqual(commits_count, 3)

    @patch("GithubAPI.requests.get")
    def test_github_info(self, mock_get):

        repo_response = Mock()
        repo_response.status_code = 200
        repo_response.text = '[{"name": "hellogitworld"}, {"name": "Mocks"}]'

        commits_response1 = Mock()
        commits_response1.status_code = 200
        commits_response1.text = '[{"sha": "123"}, {"sha": "456"}]'

        commits_response2 = Mock()
        commits_response2.status_code = 200
        commits_response2.text = '[{"sha": "789"}]'

        mock_get.side_effect = [
            repo_response,
            commits_response1,
            commits_response2
        ]

        results = github_info("richkempinski")

        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)

        repo_names = []

        for repo_name, commits in results:
            repo_names.append(repo_name)
            self.assertIsInstance(commits, int)

        self.assertIn("hellogitworld", repo_names)

    @patch("GithubAPI.requests.get")
    def test_invalid_user(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = ""
        mock_get.return_value = mock_response

        repos = get_github_repos("thisuserdoesnotexist123456789")

        self.assertIsNone(repos)


if __name__ == "__main__":
    unittest.main()
