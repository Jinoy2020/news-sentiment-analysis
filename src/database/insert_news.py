
from src.database.connection import get_connection

def insert_news(article):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO news (
            id,
            title,
            description,
            content,
            url,
            image,
            published_at,
            language,
            source_name,
            source_url,
            source_country,
            sentiment,
            sentiment_score
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        ON CONFLICT (id) DO NOTHING;
    """, (
        article.get("id"),
        article.get("title"),
        article.get("description"),
        article.get("content"),
        article.get("url"),
        article.get("image"),
        article.get("published_at"),
        article.get("language"),
        article.get("source_name"),
        article.get("source_url"),
        article.get("source_country"),
        article.get("sentiment"),
        article.get("sentiment_score"),
    ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Article inserted successfully!")

# testing the insert_news function
if __name__ == "__main__":
    test_article = {
        "id": "test-001",
        "title": "Test News Article",
        "description": "This is a test article.",
        "content": "Testing PostgreSQL RDS connection.",
        "url": "https://example.com",
        "image": None,
        "published_at": "2026-09-02 12:00:00",
        "language": "en",
        "source_name": "Test Source",
        "source_url": "https://example.com",
        "source_country": "US",
        "sentiment": "positive",
        "sentiment_score": 0.8
    }

    insert_news(test_article)