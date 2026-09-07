from src.database.connection import get_connection


def get_news(limit=50):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    title,
                    description,
                    url,
                    image,
                    published_at,
                    source_name,
                    sentiment,
                    sentiment_score
                FROM news
                ORDER BY published_at DESC
                LIMIT %s;
                """,
                (limit,)
            )

            return cursor.fetchall()

    finally:
        conn.close()


def get_sentiment_counts():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT sentiment, COUNT(*)
                FROM news
                GROUP BY sentiment;
                """
            )

            return cursor.fetchall()

    finally:
        conn.close()