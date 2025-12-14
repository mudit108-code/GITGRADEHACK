import requests
from datetime import datetime
from utils import parse_github_url

GITHUB_API = "https://api.github.com/repos"

def analyze_repository(repo_url):
    owner, repo = parse_github_url(repo_url)

    repo_api = f"{GITHUB_API}/{owner}/{repo}"
    contents_api = f"{repo_api}/contents"
    commits_api = f"{repo_api}/commits"

    repo_data = requests.get(repo_api).json()
    contents = requests.get(contents_api).json()
    commits = requests.get(commits_api, params={"per_page": 30}).json()

    file_count = 0
    dir_count = 0
    has_readme = False
    has_tests = False
    has_ci = False

    languages = {}
    commit_activity = []

    # ---------- File & Folder Analysis ----------
    if isinstance(contents, list):
        for item in contents:
            if item["type"] == "file":
                file_count += 1
                name = item["name"].lower()

                if "readme" in name:
                    has_readme = True
                if "test" in name:
                    has_tests = True
                if "yml" in name or "yaml" in name:
                    has_ci = True

            elif item["type"] == "dir":
                dir_count += 1

    # ---------- Commit Activity ----------
    if isinstance(commits, list):
        for commit in commits:
            
            if isinstance(commit, dict) and "commit" in commit:
                author_info = commit["commit"].get("author", {})
                date_str = author_info.get("date")
                if date_str:
                    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
                    commit_activity.append(str(date))

    # ---------- Language Distribution ----------
    lang_url = repo_data.get("languages_url")
    if lang_url:
        lang_resp = requests.get(lang_url)
        if lang_resp.status_code == 200:
            languages = lang_resp.json()

    
    if not languages and isinstance(contents, list):
        ext_lang_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C",
            ".cs": "C#",
            ".go": "Go",
            ".rb": "Ruby",
            ".php": "PHP",
            ".html": "HTML",
            ".css": "CSS",
            ".rs": "Rust"
        }
        for item in contents:
            if item["type"] == "file":
                for ext, lang in ext_lang_map.items():
                    if item["name"].lower().endswith(ext):
                        languages[lang] = languages.get(lang, 0) + 1

    
    unique_commit_days = len(set(commit_activity))

    return {
        
        "files": file_count,
        "directories": dir_count,

        # Documentation & Quality
        "has_readme": has_readme,
        "has_tests": has_tests,
        "has_ci": has_ci,

        # Git Activity
        "commits": len(commits) if isinstance(commits, list) else 0,
        "active_days": unique_commit_days,
        "commit_activity": commit_activity,

        # Metadata
        "language": repo_data.get("language"),
        "languages": languages,
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "open_issues": repo_data.get("open_issues_count", 0),
        "description": repo_data.get("description"),
        "created_at": repo_data.get("created_at"),
        "updated_at": repo_data.get("updated_at")
    }
