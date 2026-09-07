import sys
from pathlib import Path

import streamlit as st
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from data import get_news, get_sentiment_counts


st.set_page_config(
    page_title="News Sentiment Analysis",
    page_icon="📰",
    layout="wide",
)


# -----------------------------
# Header
# -----------------------------

st.title("📰 News Sentiment Analysis")
st.caption("Technology news • Sentiment analysis • Real-time data")


# -----------------------------
# Load data
# -----------------------------

news = get_news(50)
sentiment_counts = get_sentiment_counts()

sentiment_dict = dict(sentiment_counts)


# -----------------------------
# Summary
# -----------------------------

st.subheader("📊 Sentiment Overview")

col1, col2, col3, col4 = st.columns(4)

total = sum(sentiment_dict.values())

with col1:
    st.metric("Total Articles", total)

with col2:
    st.metric("Positive", sentiment_dict.get("positive", 0))

with col3:
    st.metric("Neutral", sentiment_dict.get("neutral", 0))

with col4:
    st.metric("Negative", sentiment_dict.get("negative", 0))


# -----------------------------
# Sentiment Chart
# -----------------------------

st.subheader("Sentiment Distribution")

chart_data = pd.DataFrame(
    {
        "Sentiment": [
            "Positive",
            "Neutral",
            "Negative",
        ],
        "Articles": [
            sentiment_dict.get("positive", 0),
            sentiment_dict.get("neutral", 0),
            sentiment_dict.get("negative", 0),
        ],
    }
)

st.bar_chart(
    chart_data.set_index("Sentiment")
)


# -----------------------------
# Filter
# -----------------------------

st.subheader("📰 Latest News")

filter_option = st.selectbox(
    "Filter by sentiment",
    [
        "All",
        "Positive",
        "Neutral",
        "Negative",
    ],
)


# -----------------------------
# Display News
# -----------------------------

for article in news:

    (
        title,
        description,
        url,
        image,
        published_at,
        source_name,
        sentiment,
        sentiment_score,
    ) = article

    if filter_option != "All":
        if sentiment.lower() != filter_option.lower():
            continue

    with st.container(border=True):

        st.markdown(f"### {title}")

        if image:
            st.image(image, width=300)

        if description:
            st.write(description)

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Source:** {source_name}")

        with col2:
            st.write(f"**Sentiment:** {sentiment}")

        st.write(
            f"**Sentiment Score:** {sentiment_score}"
        )

        if published_at:
            st.write(
                f"**Published:** {published_at}"
            )

        if url:
            st.link_button(
                "Read Full Article",
                url,
            )