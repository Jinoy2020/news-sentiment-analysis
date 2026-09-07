News Sentiment Analysis
An end-to-end cloud-based news sentiment analysis system that automatically collects technology news, analyzes sentiment, stores the results, and displays them through a real-time Streamlit dashboard.

Architecture
Amazon EventBridge (every 5 minutes)
              |
              v
         AWS Lambda
          /      \
         v        v
    GNews API    Amazon S3
         |
         v
  Sentiment Analysis
      (VADER)
         |
         v
 Amazon RDS PostgreSQL
         |
         v
 Amazon ECS Fargate
 Streamlit Dashboard
         ^
         |
      Amazon ECR
AWS Services
Amazon EventBridge — triggers Lambda every 5 minutes.

AWS Lambda — fetches, processes, and stores news.

Amazon S3 — stores raw GNews responses as JSON.

Amazon RDS PostgreSQL — stores processed articles and sentiment results.

Amazon ECR — stores Docker images.

Amazon ECS Fargate — runs the Streamlit dashboard.

Amazon CloudWatch — collects Lambda and ECS logs.

AWS IAM — manages service permissions.

GNews API — provides technology news.

Technology Stack
Python 3.13

Streamlit

PostgreSQL

psycopg2

VADER Sentiment

Requests

boto3

Docker

AWS Lambda

Amazon S3

Amazon RDS

Amazon ECR

Amazon ECS Fargate

Amazon EventBridge

GitHub

Project Structure
news-sentiment-analysis/
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── database/
│   │   ├── connection.py
│   │   ├── tables.py
│   │   └── insert_news.py
│   ├── news/
│   │   ├── gnews.py
│   │   └── processor.py
│   ├── sentiment/
│   │   └── analyzer.py
│   ├── storage/
│   │   └── s3.py
│   └── lambda_function.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
How It Works
EventBridge triggers the Lambda function every 5 minutes.

Lambda fetches recent technology news from GNews.

The article title, description, and content are combined.

VADER calculates a sentiment score and label.

The raw GNews response is uploaded to S3.

Processed articles are inserted into PostgreSQL on RDS.

Duplicate article IDs are ignored with ON CONFLICT.

The Streamlit dashboard running on ECS Fargate queries RDS and displays the latest data.

Sentiment labels are:

positive

neutral

negative

Example result:

{
    "label": "positive",
    "score": 0.91
}
Running Locally
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd news-sentiment-analysis
2. Create a virtual environment
Windows:

python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file:

GNEWS_API_KEY=your_gnews_api_key

DB_HOST=your_rds_endpoint
DB_PORT=5432
DB_NAME=news_sentiment
DB_USER=postgres
DB_PASSWORD=your_database_password
Never commit .env or credentials to GitHub.

5. Run the news pipeline
python -m src.news.gnews
6. Run the Streamlit dashboard
streamlit run dashboard/app.py
Open:

http://localhost:8501
Docker
Lambda
Build the Lambda image:

docker build --provenance=false -t news-sentiment-lambda:latest .
The image is pushed to Amazon ECR and deployed as a container-image Lambda function.

Dashboard
Build:

docker build -f dashboard/Dockerfile -t news-sentiment-dashboard:latest .
Run locally:

docker run --env-file .env -p 8501:8501 news-sentiment-dashboard:latest
Open:

http://localhost:8501
Deployment Flow
Source Code
    |
  Docker
    |
  Amazon ECR
    |
    +----> AWS Lambda
    |
    +----> Amazon ECS Fargate
                 |
                 v
        Streamlit Dashboard
Database
The PostgreSQL news table stores:

Article ID

Title

Description

Content

URL

Image

Published timestamp

Language

Source name

Source URL

Source country

Sentiment

Sentiment score

Security Notes
API keys and database passwords are stored in environment variables.

.env is excluded from Git.

AWS credentials are not included in Docker images.

Lambda uses an IAM execution role for AWS access.

The current RDS configuration allows PostgreSQL access from the internet because Lambda is not connected to a VPC. This is a simplified project/demo configuration and is not recommended for production.

A production setup should use private networking, restricted security groups, and a secrets manager.

Monitoring
Amazon CloudWatch is used for:

Lambda execution logs

Lambda errors and timeouts

ECS container logs

Dashboard troubleshooting

Git Workflow
The project uses separate branches for team members.

git checkout main
git pull origin main

git checkout person1
git merge main

git add .
git commit -m "Describe the change"
git push origin person1
Changes are merged into main through pull requests and review.

Team Contribution
The project was developed as a two-person team with contributions across:

News collection and processing

Sentiment analysis

PostgreSQL/RDS

S3 storage

Lambda

EventBridge

Streamlit dashboard

Docker and ECR

ECS Fargate

Integration and testing

Current Status
The complete pipeline has been successfully tested:

EventBridge
     ↓
Lambda
     ↓
GNews API
     ↓
VADER Sentiment Analysis
     ↓
S3 + PostgreSQL RDS
     ↓
ECS Fargate
     ↓
Streamlit Dashboard
The dashboard receives live data from PostgreSQL, while EventBridge automatically triggers Lambda every 5 minutes.

Future Improvements
Move Lambda into a VPC with restricted RDS access.

Place ECS behind an Application Load Balancer.

Use AWS Secrets Manager for database credentials.

Add dashboard authentication.

Add more news categories and sources.

Add historical sentiment trends and filtering.

Add automated tests and CI/CD.

