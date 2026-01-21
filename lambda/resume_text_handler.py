import boto3
import uuid
import json

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ResumeData')

TARGET_SKILLS = [
    'aws',
    'lambda',
    'dynamodb',
    's3',
    'cloud',
    'serverless'
]

def calculate_score(text):
    text_lower = text.lower()
    matched_skills = []

    for skill in TARGET_SKILLS:
        if skill in text_lower:
            matched_skills.append(skill)

    skill_score = int((len(matched_skills) / len(TARGET_SKILLS)) * 70)
    keyword_score = 30 if len(matched_skills) >= 3 else 10

    total_score = skill_score + keyword_score
    return total_score, matched_skills

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))

    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode('utf-8')

    score, matched_skills = calculate_score(text)

    resume_id = str(uuid.uuid4())

    item = {
        'resumeId': resume_id,
        'fileName': key,
        'resumeText': text,
        'score': score,
        'matchedSkills': matched_skills
    }

    print("SCORE RESULT:", item)

    table.put_item(Item=item)

    return {
        'status': 'success',
        'resumeId': resume_id,
        'score': score
    }