def generate_personalized_roadmap(scores):
    roadmap = []

    # ---------------- Documentation ----------------
    if scores.get("Documentation", 0) < 10:
        roadmap.append(
            "Documentation Gap: Create a comprehensive README including project overview, "
            "architecture explanation, setup instructions and sample outputs."
        )
    else:
        roadmap.append(
            "Documentation Strength: Improve README further by adding diagrams, screenshots, "
            "and contribution guidelines."
        )

    # ---------------- Testing & Maintainability ----------------
    if scores.get("Testing & Maintainability", 0) < 10:
        roadmap.append(
            "Testing Gap: Add unit tests using pytest and aim for at least 70% coverage to "
            "improve code reliability."
        )
    else:
        roadmap.append(
            "Testing Strength: Expand test suite with edge cases and integration tests."
        )

    # ---------------- Git Practices ----------------
    if scores.get("Git Practices", 0) < 10:
        roadmap.append(
            "Version Control Improvement: Commit more frequently, use meaningful commit messages, "
            "and avoid pushing large unreviewed changes."
        )
    else:
        roadmap.append(
            "Git Hygiene Strength: Introduce feature branches and pull requests for structured development."
        )

    # ---------------- Code Quality & Structure ----------------
    if scores.get("Code Quality & Structure", 0) < 15:
        roadmap.append(
            "Code Structure Improvement: Refactor the project into modular components, "
            "separate business logic from UI and follow naming conventions."
        )
    else:
        roadmap.append(
            "Code Quality Strength: Improve readability further by adding docstrings and type hints."
        )

    # ---------------- Project Relevance ----------------
    if scores.get("Project Relevance", 0) < 12:
        roadmap.append(
            "Relevance Boost: Extend the project with a real world feature, API integration "
            "or performance optimization to increase practical value."
        )
    else:
        roadmap.append(
            "Project Depth Strength: Consider turning this into an open-source project or case study."
        )

    # ---------------- Advanced Growth (Always Shown) ----------------
    roadmap.extend([
        "Automation: Add CI/CD using GitHub Actions for automated testing and linting.",
        "Quality Assurance: Integrate code linters and formatters.",
        "Monitoring: Use GitHub Issues and Projects to track bugs, enhancements and milestones.",
        "Career Readiness: Write a short project summary explaining design decisions as if presenting to a recruiter."
    ])

    return roadmap



def generate_30_day_plan(mode, scores):
    
    return generate_personalized_roadmap(scores)
