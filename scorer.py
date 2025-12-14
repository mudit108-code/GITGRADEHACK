def score_profile(profile_data):
    

    breakdown = {
        "Activity & Consistency": 0,
        "Tech Stack Depth": 0,
        "Profile Maturity": 0,
        "Open Source Readiness": 0
    }

    # Activity & Consistency
    if profile_data["repos"] >= 10:
        breakdown["Activity & Consistency"] = 25
    elif profile_data["repos"] >= 5:
        breakdown["Activity & Consistency"] = 18
    else:
        breakdown["Activity & Consistency"] = 10

    # Tech Stack Depth
    lang_count = len(profile_data["languages"])
    if lang_count >= 5:
        breakdown["Tech Stack Depth"] = 25
    elif lang_count >= 3:
        breakdown["Tech Stack Depth"] = 18
    else:
        breakdown["Tech Stack Depth"] = 10

    # Profile Maturity
    if profile_data["followers"] >= 10:
        breakdown["Profile Maturity"] = 25
    else:
        breakdown["Profile Maturity"] = 15

    # Open Source Readiness
    breakdown["Open Source Readiness"] = 25 if profile_data["repos"] >= 3 else 15

    total_score = sum(breakdown.values())
    return total_score, breakdown


def score_repository(repo_data):
    

    breakdown = {
        "Code Quality & Structure": 0,
        "Documentation": 0,
        "Testing & Maintainability": 0,
        "Git Practices": 0,
        "Project Relevance": 0
    }

    # Code Quality & Structure
    if repo_data["files"] >= 20:
        breakdown["Code Quality & Structure"] = 25
    elif repo_data["files"] >= 10:
        breakdown["Code Quality & Structure"] = 18
    else:
        breakdown["Code Quality & Structure"] = 10

    # Documentation
    breakdown["Documentation"] = 15 if repo_data["has_readme"] else 5

    # Testing
    breakdown["Testing & Maintainability"] = 20 if repo_data["has_tests"] else 5

    # Git Practices
    if repo_data["active_days"] >= 10:
        breakdown["Git Practices"] = 20
    elif repo_data["active_days"] >= 5:
        breakdown["Git Practices"] = 12
    else:
        breakdown["Git Practices"] = 5

    # Project Relevance
    relevance = 10
    if repo_data["description"]:
        relevance += 5
    if repo_data["stars"] > 0:
        relevance += 5
    breakdown["Project Relevance"] = relevance

    total_score = sum(breakdown.values())
    return total_score, breakdown
