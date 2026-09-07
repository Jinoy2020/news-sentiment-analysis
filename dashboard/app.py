import sys
from pathlib import Path

import streamlit as st

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from data import get_news, get_sentiment_counts


st.set_page_config(
    page_title="News Sentiment Analysis",
    page_icon="📰",
    layout="wide",
)

st.title("📰 News Sentiment Analysis")
st.write("Latest technology news and sentiment analysis")


# Load data
news = get_news()
sentiment_counts = get_sentiment_counts()


# Sentiment summary
st.subheader("Sentiment Summary")

col1, col2, col3 = st.columns(3)

sentiment_dict = dict(sentiment_counts)

with col1:
    st.metric("Positive", sentiment_dict.get("positive", 0))

with col2:
    st.metric("Neutral", sentiment_dict.get("neutral", 0))

with col3:
    st.metric("Negative", sentiment_dict.get("negative", 0))


# News
st.subheader("Latest News")

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

    st.markdown(f"### {title}")

    if description:
        st.write(description)

    st.write(f"**Source:** {source_name}")
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Score:** {sentiment_score}")

    if url:
        st.link_button("Read Article", url)

    st.divider()