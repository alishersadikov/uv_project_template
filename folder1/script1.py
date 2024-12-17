import requests

response = requests.get("https://api.github.com")
print("Folder 1: GitHub API Status:", response.status_code)
