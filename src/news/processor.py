def process_articles(articles):
    """Clean and standardize raw GNews articles.

    Args:
        articles (list): Raw article dictionaries from GNews.

    Returns:
        list: Cleaned article dictionaries.
    """
    processed_articles = []

    for article in articles:
        processed_article = {
            "id": article.get("id"),
            "title": article.get("title"),
            "description": article.get("description"),
            "content": article.get("content"),
            "url": article.get("url"),
            "image": article.get("image"),
            "published_at": article.get("publishedAt"),
            "language": article.get("lang"),
            "source_name": article.get("source", {}).get("name"),
            "source_url": article.get("source", {}).get("url"),
            "source_country": article.get("source", {}).get("country"),
        }

        processed_articles.append(processed_article)

    return processed_articles