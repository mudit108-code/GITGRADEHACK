import requests
from utils import parse_profile_url
from datetime import datetime

def analyze_profile(profile_url):
    username = parse_profile_url(profile_url)
    user_api = f"https://api.github.com/users/{username}"
    repos_api = f"https://api.github.com/users/{username}/repos"

    user = requests.get(user_api).json()

    
    repos = []
    page = 1
    per_page = 100  
    while True:
        response = requests.get(f"{repos_api}?per_page={per_page}&page={page}").json()
        if not response:
            break
        repos.extend(response)
        page += 1

    languages = {}
    for repo in repos:
        if repo["language"]:
            languages[repo["language"]] = languages.get(repo["language"], 0) + 1

    
    created_at = datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    account_age_years = round((datetime.utcnow() - created_at).days / 365, 1)

    return {
        "repos": len(repos),
        "followers": user["followers"],
        "account_age": account_age_years,
        "languages": languages
    }
