def parse_github_url(url):
    parts = url.rstrip("/").split("/")
    return parts[-2], parts[-1]


def parse_profile_url(url):
    parts = url.rstrip("/").split("/")
    return parts[-1]
