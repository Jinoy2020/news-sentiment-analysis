import os
import requests
from dotenv import load_dotenv

from src.news.processor import process_articles
from src.storage.s3 import upload_raw_news
from src.database.insert_news import insert_news


load_dotenv()


def fetch_news():
    """Fetch recent technology news from the GNews API.

    Returns:
        dict: JSON response containing news articles.

    Raises:
        ValueError: If the GNews API key is not configured.
        requests.RequestException: If the API request fails.
    """
    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        raise ValueError("GNEWS_API_KEY is not set in the .env file.")

    url = "https://gnews.io/api/v4/search"

    params = {
        "q": "technology",
        "lang": "en",
        "max": 10,
        "apikey": api_key,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    news = fetch_news()

    # Upload raw GNews response to S3
    upload_raw_news(news)

    articles = news.get("articles", [])

    print(f"Found {len(articles)} raw articles.")

    processed_articles = process_articles(articles)

    print(f"Processed {len(processed_articles)} articles.")

    # Insert processed articles into PostgreSQL
    for article in processed_articles:
        insert_news(article)

    print(f"Inserted {len(processed_articles)} articles into PostgreSQL.")