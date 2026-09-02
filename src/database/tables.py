from src.database.connection import get_connection


def create_news_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id VARCHAR(255) PRIMARY KEY,
            title TEXT,
            description TEXT,
            content TEXT,
            url TEXT,
            image TEXT,
            published_at TIMESTAMP,
            language VARCHAR(10),
            source_name VARCHAR(255),
            source_url TEXT,
            source_country VARCHAR(10),
            sentiment VARCHAR(20),
            sentiment_score FLOAT
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("News table created successfully!")


if __name__ == "__main__":
    create_news_table()