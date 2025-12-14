# GitHub Sense AI

AI powered Developer & Repository Evaluation Tool

GitHub Sense AI is a web application that analyzes GitHub profiles and repositories to provide actionable insights. It generates a score, detailed summary, visualizations and a personalized roadmap for developers, helping them understand strengths and weaknesses in their coding projects or contributions.

## Features
Profile Analyzer

Evaluates GitHub user profiles:

Number of repositories, followers and account age.

Languages used across repositories.

Personalized skill breakdown.

Visualizations:

Radar chart of skills.

Bar chart of language distribution.

Personalized  roadmap to improve coding skills and profile.

Repository Analyzer:

Analyzes public GitHub repositories:

Folder structure and file count.

Code quality indicators: README, tests, CI/CD files.

Commit history and consistency.

Stars, forks, open issues and languages.

Visualizations:

Radar chart of repository quality.

Commit activity chart.

Language distribution.

Personalized improvement roadmap with actionable steps.

### Installation
Prerequisites:

Python 3.10+

Git installed on your system

GitHub account (public profiles/repositories required)

Step 1: Clone the repository

Step 2: Create a virtual environment (recommended)
python -m venv venv


Activate the virtual environment:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt

#### How to Run

Open VS Code (or any IDE) in the project directory.

Run the Streamlit app:

streamlit run app.py


Enter a GitHub profile URL or repository URL in the input box.

Select the analysis mode: Profile Analyzer or Repository Analyzer.


Click Analyze to view metrics, visualizations and roadmap.
