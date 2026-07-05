import streamlit as st
import plotly.express as px
import pandas as pd


def show_charts(score, confidence, fluency, clarity):

    st.subheader("📈 AI Performance Analytics")

    df = pd.DataFrame({
        "Category": [
            "Concept",
            "Confidence",
            "Fluency",
            "Clarity"
        ],
        "Score": [
            score,
            confidence,
            fluency,
            clarity
        ]
    })

    fig = px.bar(
        df,
        x="Category",
        y="Score",
        color="Category",
        text="Score",
       
        color_discrete_sequence=[
        "#3B82F6",   # Blue
        "#60A5FA",   # Light Blue
        "#7C3AED",   # Purple
        "#22C55E"    # Green
         ]
    )

    fig.update_traces(
        textposition="outside",
        marker_line_color="white",
        marker_line_width=1.5
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",

        font=dict(
            color="white",
            size=14
        ),

        xaxis=dict(
            title="",
            tickfont=dict(color="white")
        ),

        yaxis=dict(
            title="Score (%)",
            range=[0, 100],
            tickfont=dict(color="white"),
            gridcolor="rgba(255,255,255,0.1)"
        ),

        height=400,
        showlegend=False,
        margin=dict(
            l=40,
            r=20,
            t=60,
            b=40
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )