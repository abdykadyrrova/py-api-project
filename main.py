import requests

response = requests.get("https://api.github.com/users/abdykadyrrova/repos") # get names of the repos for the user
my_repos = response.json()

for repo in my_repos:
    print(f'Repo Name: {repo["name"]}. Repo URL: {repo["html_url"]}.')
