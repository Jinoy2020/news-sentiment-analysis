from src.news.gnews import fetch_news
from src.news.processor import process_articles
from src.storage.s3 import upload_raw_news
from src.database.insert_news import insert_news


def lambda_handler(event, context):
    news = fetch_news()

    # Upload raw GNews response to S3
    upload_raw_news(news)

    articles = news.get("articles", [])

    print(f"Found {len(articles)} raw articles.")

    processed_articles = process_articles(articles)

    print(f"Processed {len(processed_articles)} articles.")

    for article in processed_articles:
        insert_news(article)

    print(f"Inserted {len(processed_articles)} articles into PostgreSQL.")

    return {
        "statusCode": 200,
        "message": f"Processed and inserted {len(processed_articles)} articles."
    }