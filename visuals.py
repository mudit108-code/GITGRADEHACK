import plotly.graph_objects as go
import plotly.express as px


def radar_chart(category_scores, title="Repository Skill Profile"):
    labels = list(category_scores.keys())
    values = list(category_scores.values())

    
    labels.append(labels[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            name="Score",
            line=dict(width=3),
            marker=dict(size=6),
            opacity=0.85
        )
    )

    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            font=dict(size=18)
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 25],
                tickfont=dict(size=10),
                tickvals=[5, 10, 15, 20, 25],
                gridcolor="lightgray"
            ),
            angularaxis=dict(
                tickfont=dict(size=11)
            )
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40),
        template="plotly_white"
    )

    return fig


def progress_bar_chart(category_scores, title="Category-wise Breakdown"):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=list(category_scores.values()),
            y=list(category_scores.keys()),
            orientation="h",
            text=[f"{v}/25" for v in category_scores.values()],
            textposition="auto"
        )
    )

    fig.update_layout(
        title=dict(text=title, x=0.5),
        xaxis=dict(range=[0, 25], title="Score"),
        yaxis=dict(title="Category"),
        template="plotly_white",
        height=350
    )

    return fig


def commit_activity_chart(commit_counts):
    fig = px.line(
        y=commit_counts,
        markers=True,
        title="Commit Activity Over Time"
    )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Commits",
        template="plotly_white"
    )

    return fig


def language_distribution_chart(language_data):
    fig = px.pie(
        names=list(language_data.keys()),
        values=list(language_data.values()),
        title="Language Usage Distribution",
        hole=0.4
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig
