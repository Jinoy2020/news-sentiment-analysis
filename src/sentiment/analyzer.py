from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    """Analyze the sentiment of a piece of text.

    Returns:
        dict: Sentiment label and compound score.
    """

    if not text:
        return {
            "label": "neutral",
            "score": 0.0
        }

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "score": compound
    }

# for testing
if __name__ == "__main__":
    texts = [
        "Apple reported excellent financial results.",
        "The company suffered a major loss.",
        "Apple announced a new product today."
    ]

    for text in texts:
        result = analyze_sentiment(text)

        print(f"\nText: {text}")
        print(f"Sentiment: {result['label']}")
        print(f"Score: {result['score']}")

