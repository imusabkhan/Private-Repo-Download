from github import Github
import os

# Replace with your GitHub username and personal access token
username = 'USERNAME'
access_token = 'YOUR_GITHUB_TOKEN'

# Path where repositories will be downloaded
download_path = 'private_repositories'

# Authenticate with GitHub
g = Github(username, access_token)

# Get the authenticated user
user = g.get_user()

# Retrieve a list of all private repositories
repositories = user.get_repos(type='private')

# Create the download directory if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Clone or download each repository
for repo in repositories:
    repo_name = repo.full_name
    repo_path = os.path.join(download_path, repo_name)
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
    os.system(f'git clone {repo.clone_url} {repo_path}')
    print(f"Downloaded repository: {repo_name}")
