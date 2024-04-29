If you find my work helpful and would like to show your support, you can buy me a coffee! ☕

<a href="https://www.buymeacoffee.com/imusabkhan" target="_blank">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;">
</a>


# GitHub Private Repository Downloader

This Python script allows you to download all your private repositories from GitHub to your local machine.

## Prerequisites

- Python 3 installed on your machine.
- GitHub account with private repositories.
- Personal Access Token from GitHub with permissions to access your repositories.

## Setup

1. Clone this repository or download the script `private_repo_down.py`.
2. Install the required Python packages using pip:

   ```bash
   pip install PyGithub
3. Replace the placeholder values in the script with your GitHub username and Personal Access Token.

## Usage
1. Run the script `python3 private_repo_down.py`.
2. It will authenticate with your GitHub account and fetch a list of your private repositories.
3. The script will create a directory specified in download_path (by default private_repositories) if it doesn't exist.
4. Each repository will be cloned or downloaded into the specified directory.

## Configuration
1. `username`: Your GitHub username.
2. `access_token`: Your Personal Access Token generated from GitHub.
3. `download_path`: The directory where repositories will be downloaded. Change this according to your preference.

## Notes
1. Ensure that your Personal Access Token has the necessary permissions to access your private repositories.
2. This script uses the `PyGithub` library to interact with the GitHub API.
3. Make sure you have enough disk space to download all your repositories.

## Social Profiles

[Medium](https://medium.com/@imusabkhan) |
[YouTube](https://www.youtube.com/musabkhan) |
[LinkedIn](https://www.linkedin.com/in/musab1995/) |
[Twitter](https://twitter.com/Musab1995) |
[HackerOne](https://hackerone.com/musabkhan) |
[Facebook](https://facebook.com/imusabkhan) |
[Instagram](https://instagram.com/imusabkhan)

## Disclaimer
This script is provided as-is and the author takes no responsibility for any damages caused by its usage. Use it responsibly and ensure that you have proper permissions to access the repositories you're downloading.
