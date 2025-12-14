import streamlit as st
from profile_analyzer import analyze_profile
from repo_analyzer import analyze_repository
from visuals import radar_chart, language_distribution_chart, commit_activity_chart
from scorer import score_profile, score_repository
from roadmap import generate_30_day_plan

st.set_page_config(page_title="GitHub Sense AI", layout="wide")

st.title("Github Sense AI")
st.caption("AI powered Developer & Repository Evaluation")

mode = st.selectbox(
    "Select Analysis Mode",
    ["Profile Analyzer", "Repository Analyzer"]
)

github_input = st.text_input("Enter GitHub Profile or Repository URL")

if st.button("Analyze"):
    if mode == "Profile Analyzer":
        profile_data = analyze_profile(github_input)
        score, breakdown = score_profile(profile_data)

        # ---------- Profile Metrics Row ----------
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Developer Score", f"{score}/100")
        col2.metric("Repositories", profile_data["repos"])
        col3.metric("Followers", profile_data["followers"])
        col4.metric("Account Age (Years)", profile_data["account_age"])

        
        st.plotly_chart(radar_chart(breakdown), use_container_width=True)

        # Language distribution
        st.subheader("Language Distribution")
        sorted_languages = dict(sorted(profile_data["languages"].items(), key=lambda x: x[1], reverse=True))
        st.plotly_chart(language_distribution_chart(sorted_languages))

        # Personalized roadmap
        st.subheader("Personalized Growth Plan")
        for step in generate_30_day_plan("profile", breakdown):
            st.markdown(f"- {step}")

    else:
        repo_data = analyze_repository(github_input)
        score, breakdown = score_repository(repo_data)

        # ---------- Repository Metrics Row ----------
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Repository Score", f"{score}/100")
        col2.metric("Stars", repo_data.get("stars", 0))
        col3.metric("Forks", repo_data.get("forks", 0))
        col4.metric("Open Issues", repo_data.get("open_issues", 0))
        col5.metric("Directories", repo_data.get("directories", 0))

        st.plotly_chart(radar_chart(breakdown), use_container_width=True)

        # Languages distribution chart
        st.subheader("Languages Used")
        languages = repo_data.get("languages", {})
        sorted_languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))
        st.plotly_chart(language_distribution_chart(sorted_languages))

        # Commit activity chart
        st.subheader("Commit Activity")
        st.plotly_chart(commit_activity_chart(repo_data["commit_activity"]))

        # README, Tests, CI/CD Status
        st.subheader("Quality & CI/CD")
        readme_status = "Yes" if repo_data.get("has_readme") else "No"
        tests_status = "Yes" if repo_data.get("has_tests") else "No"
        ci_status = "Yes" if repo_data.get("has_ci") else "No"
        st.markdown(f"- README: {readme_status}")
        st.markdown(f"- Tests: {tests_status}")
        st.markdown(f"- CI/CD: {ci_status}")

        # Repository roadmap
        st.subheader("Repository Improvement Plan")
        for step in generate_30_day_plan("repo", breakdown):
            st.markdown(f"- {step}")
