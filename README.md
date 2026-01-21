# Resume Score API (AWS Serverless)

A production-style serverless backend built using AWS services.

## Tech Stack
- AWS Lambda
- API Gateway (HTTP API)
- DynamoDB
- S3
- CloudWatch
- Python

## Features
- Upload resume text
- Score resume based on skills
- REST API endpoints
- Fully serverless architecture


## Architecture
- API Gateway exposes REST endpoints
- AWS Lambda handles business logic
- DynamoDB stores resume data and scores
- Serverless architecture (no servers managed)

## API Endpoints

POST /resume/text  
- Accepts raw resume text
- Stores processed content in DynamoDB

GET /resume/{resumeId}/score  
- Calculates skill match score
- Returns score and matched skills

## Lambda Functions
- get_resume_score.py  
  Calculates skill match score from resume text

- resume_text_handler.py  
  Extracts and preprocesses resume content

## Status
✅ Deployed and tested on AWS (ap-south-1)

## Highlights
- Stateless Lambda functions
- DynamoDB used for low-latency access
- Designed to scale automatically with traffic
- Zero server management (fully serverless)