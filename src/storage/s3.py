import json
from datetime import datetime, timezone

import boto3


BUCKET_NAME = "news-sentiment-raw"

s3 = boto3.client("s3")


def upload_raw_news(news_data):
    """Upload raw GNews response to S3."""

    timestamp = datetime.now(timezone.utc).strftime("%Y/%m/%d/%H%M%S")

    key = f"raw-news/{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(news_data, indent=2),
        ContentType="application/json",
    )

    print(f"Uploaded raw news to s3://{BUCKET_NAME}/{key}")

    return key


if __name__ == "__main__":
    test_data = {
        "message": "S3 connection test",
        "status": "success"
    }

    upload_raw_news(test_data)