import json

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    try:
        path = event.get("rawPath", "")
        params = event.get("pathParameters") or {}
        resume_id = params.get("resumeId")

        if not resume_id:
            return response(400, {"error": "resumeId missing"})

        # Route: /resume/{resumeId}/summary
        if path.endswith("/summary"):
            return response(200, {
                "resumeId": resume_id,
                "summary": "This is a generated resume summary",
                "score": 78
            })

        # Route: /resume/{resumeId}
        if path.endswith(resume_id):
            return response(200, {
                "resumeId": resume_id,
                "name": "Test User",
                "skills": ["AWS", "Lambda", "API Gateway"],
                "score": 78
            })

        return response(404, {"error": "Route not handled"})

    except Exception as e:
        return response(500, {
            "error": "Internal Server Error",
            "details": str(e)
        })