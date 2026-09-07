
f38d72d6-59fb-47f6-bda4-3fe43149fcef.png

5c300a53-c72e-42c9-b089-c0b3d5a93e0e.png
 how do i know if the event bridge is working , should i wait 5 mins?

4b4e7b8a-ecde-4005-b1a7-c7a3cbc24f7c.png
 after waiting 5 mins  i dont see any cahnges

fdfe24aa-dd28-48d7-972d-721b927d1727.png

3aa41358-6718-4592-ab4b-d1821040ac02.png

1fe0a1e6-212e-467c-98c0-6666c62ff532.png
still

b77b87bd-6655-4ec8-8549-9f335f659cd0.png
now 41

1273aae6-3c98-414e-ae58-cfb24522ae71.jpeg

ee88e041-bd96-4a17-be7a-535ff1d736b7.png
ok now , its now updating? any problem?

6bf07e2d-5b4c-45bf-a1f6-2ee9789b75db.png
838fa656-fb65-48af-a3d9-575e5cb28f25.png
?

38c644e3-b871-4a1a-a7ed-d4d3756b3111.png
is this now complete

9a6acd8b-1375-4437-8a28-aee4fe6792f2.png

2cc73e19-062d-496b-962a-4b1f8510880b.png
f59b2d45-a764-4a63-be9c-97004d24df3d.png

2d31a4ce-a614-43d6-90f0-54cd2332d305.png

c6e106c7-7e10-4c33-a59f-6f353090d3ca.png
ea99e5a6-e3e9-49dd-ae09-3cea872480f1.png

b7fa74f2-9380-4841-b3ce-84d9500ff768.png

9563ff9f-79f9-4c44-9e75-a15537a3fc10.png

b9b3995a-cb1c-4de7-ae1a-8b612a7dac75.png

d676edca-2526-442c-8828-a499ef65ee66.png

05af5904-d875-4801-b68d-e60b8d27e30d.png

0271828c-c10d-4ca7-98c6-648db5e62bbe.png

01e7e890-48aa-4b84-9bfe-9d5e66ea4262.png

26104fe8-742c-45c5-a575-0cf7887af225.png

79249457-df1b-4a22-a0fc-83a75371540e.png
 how\

7a917a19-2030-414f-97f5-5f65a5400591.png

f36e0d59-9b36-4158-b0bd-b93e778ae416.png

5f4b890c-f610-43c7-843a-5c6d6b3b8cf5.png

0f26f267-ec4b-4618-8d06-af3c353200ce.png
is this now complete

51d93e74-596a-4230-bf42-d05d015028f8.png

fd8b8de2-d75b-46a4-9086-ddcbf67c6b0c.png
 btw is it complete , do we used all necessary things?

Yes 👍 Now let's commit the final changes to GitHub.

We'll do it one step at a time.

Step 1 — Check which branch you're on
Open your terminal inside:

C:\JINOY\INTERN\news-sentiment-analysis
Run:

git branch
Send me the output. Don't commit yet.


ok now commit text?

If you're committing the final AWS deployment/architecture updates, use:

git add .
git commit -m "Finalize AWS deployment and architecture"
Then push your current branch:

git push origin person1
If you're on person2, use:

git push origin person2
Best commit message:

Finalize AWS deployment and architecture

This covers the Lambda, EventBridge, S3, RDS, ECS, ECR, and dashboard deployment work without making the commit message unnecessarily long.


now create the readme

Done — I created a complete README.md for your project, covering the architecture, AWS services, setup, Docker, deployment, database, security, Git workflow, team contribution, and future improvements.

Download README.md

Next step
Put this file in your project root:

news-sentiment-analysis/
├── README.md  ← replace your current one
├── dashboard/
├── src/
├── Dockerfile
├── requirements.txt
└── ...
Then we'll do:

git add README.md
git commit -m "Add comprehensive project README"
git push origin person1
Don't run these yet if you're on a different branch—tell me when you've replaced the README and we'll do the commit step together. 


README.md
Document


Library
/
README.md


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

