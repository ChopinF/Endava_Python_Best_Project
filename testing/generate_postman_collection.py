import json
import uuid
from pathlib import Path

# Load test cases
with open(r"testing\manual_test_cases.json", encoding="utf-8") as f:
    test_cases = json.load(f)

# Helper to create Postman request item
def create_postman_request(name, method, url, body=None, headers=None):
    return {
        "name": name,
        "request": {
            "method": method,
            "header": [
                {"key": k, "value": v, "type": "text"} for k, v in (headers or {}).items()
            ],
            "url": {
                "raw": "{{base_url}}" + url,
                "host": ["{{base_url}}"],
                "path": url.strip("/").split("/")
            },
            "body": {
                "mode": "raw",
                "raw": json.dumps(body, indent=2)
            } if method in ("POST", "PUT") else None
        },
        "response": []
    }

# Create the Postman collection
collection = {
    "info": {
        "name": "FastAPI Math Microservice",
        "_postman_id": str(uuid.uuid4()),
        "description": "Postman collection generated for FastAPI factorial, fibo, and pow endpoints.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": []
}

# Organize by folder
for group, cases in test_cases.items():
    folder = {
        "name": group.upper(),
        "item": []
    }
    for case in cases:
        method = case.get("method", "POST")
        headers = case.get("headers", {"name": "key"})
        body = case.get("input")
        if group == "pow":
            url = f"/pow/{case.get('type', 'int')}"
        elif group == "fibo":
            url = "/fibo/retrieve"
        elif group == "fact":
            url = "/fact/retrieve"
        else:
            url = case.get("endpoint", "/unknown")
        folder["item"].append(create_postman_request(case["test_id"], method, url, body, headers))
    collection["item"].append(folder)

# Save to file
output_path = Path("testing\postman_collection_microservice.json")
with open(output_path, "w") as f:
    json.dump(collection, f, indent=2)

print(f"Postman collection saved to: {output_path}")
