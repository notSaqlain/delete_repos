import os
import requests
from dotenv import load_dotenv

# Load environment variables from the local .env file
load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

# List the exact names of the repositories you want to delete
REPOS_TO_DELETE = [
    "Java-World",
    "La-citta-degli-eventi",
    "Guess-number",
    "Frigorifero",
    "java",
    "Barca",
    "HTML-JS",
    "Generics",
    "Bambino",
    "Java-Inheritance",
    "private1",
    "Serie-A",
    "private",
    "Poste_Italine"
]

# Validation check
if not TOKEN or not USERNAME:
    print("Error: Missing GITHUB_USERNAME or GITHUB_TOKEN in your .env file.")
    exit(1)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

print(f"Connecting to GitHub as: {USERNAME}\n")

for repo in REPOS_TO_DELETE:
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"Successfully deleted: {repo}")
    else:
        error_message = response.json().get('message', 'Unknown error')
        print(f"Failed to delete '{repo}': {error_message}")
