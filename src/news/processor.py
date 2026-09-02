
from src.sentiment.analyzer import analyze_sentiment

def process_articles(articles):
    """Clean articles and add sentiment analysis."""

    processed_articles = []

    for article in articles:
        title = article.get("title")
        description = article.get("description")
        content = article.get("content")

        # Use title + description for sentiment analysis
        text = " ".join(
            part for part in [title, description, content]
            if part
        )

        sentiment_result = analyze_sentiment(text)

        processed_article = {
            "id": article.get("id"),
            "title": title,
            "description": description,
            "content": content,
            "url": article.get("url"),
            "image": article.get("image"),
            "published_at": article.get("publishedAt"),
            "language": article.get("lang"),
            "source_name": article.get("source", {}).get("name"),
            "source_url": article.get("source", {}).get("url"),
            "source_country": article.get("source", {}).get("country"),
            "sentiment": sentiment_result["label"],
            "sentiment_score": sentiment_result["score"],
        }

        processed_articles.append(processed_article)

    return processed_articles