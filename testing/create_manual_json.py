import json
from pathlib import Path

# Define test inputs and expected outputs in structured JSON format
test_cases = {
    "pow": [
        {
            "test_id": "POW-01",
            "input": {"a": 2, "b": 3},
            "type": "int",
            "expected_output": {"result": 8}
        },
        {
            "test_id": "POW-02",
            "input": {"a": 4, "b": 0.5},
            "type": "float",
            "expected_output": {"result": 2.0}
        },
        {
            "test_id": "POW-03",
            "input": {"a": "1+1j", "b": "2"},
            "type": "complex",
            "expected_output": {"result": "2j"}
        },
        {
            "test_id": "POW-04",
            "input": {"a": "a", "b": "b"},
            "type": "int",
            "expected_output": {"error": "422 Unprocessable Entity"}
        },
    ],
    "fibo": [
        {
            "test_id": "FIB-01",
            "input": {"number": 6},
            "expected_output": {"result": 13}
        },
        {
            "test_id": "FIB-02",
            "input": {"number": 0},
            "expected_output": {"result": 1}
        },
        {
            "test_id": "FIB-03",
            "input": {"number": -1},
            "expected_output": {"error": "422 Unprocessable Entity"}
        }
    ],
    "fact": [
        {
            "test_id": "FAC-01",
            "input": {"number": 5},
            "expected_output": {"result": 120}
        },
        {
            "test_id": "FAC-02",
            "input": {"number": 0},
            "expected_output": {"result": 1}
        },
        {
            "test_id": "FAC-03",
            "input": {"number": 100},
            "expected_output": {"result": "large number"}
        },
        {
            "test_id": "FAC-04",
            "input": {"number": -5},
            "expected_output": {"error": "422 Unprocessable Entity"}
        }
    ],
    "auth": [
        {
            "test_id": "AUTH-01",
            "description": "Access with valid API key",
            "headers": {"name": "key"},
            "endpoint": "/pow/int",
            "method": "POST",
            "input": {"a": 2, "b": 2},
            "expected_output": {"result": 4}
        },
        {
            "test_id": "AUTH-02",
            "description": "Access without API key",
            "headers": {},
            "endpoint": "/pow/int",
            "method": "POST",
            "input": {"a": 2, "b": 2},
            "expected_output": {"error": "403 Forbidden"}
        }
    ],
    "extended_fact_tests": [
    {
        "test_id": "FACT-ROOT",
        "description": "Root GET returns health message",
        "method": "GET",
        "endpoint": "/fact/",
        "expected_output": "good fact"
    },
    {
        "test_id": "FACT-DELETE",
        "description": "Delete cache with API key",
        "method": "DELETE",
        "endpoint": "/fact/",
        "headers": { "name": "key" },
        "expected_output": {"type": "list"}
    },
    {
        "test_id": "FACT-POPULATE-01",
        "description": "Populate up to 5",
        "method": "POST",
        "endpoint": "/fact/",
        "headers": { "name": "key" },
        "input": {"number": 5},
        "expected_output": {"status": "204 or empty"}
    },
    {
        "test_id": "FACT-RETRIEVE-VALID",
        "description": "Retrieve factorial of 5",
        "method": "POST",
        "endpoint": "/fact/retrieve",
        "headers": { "name": "key" },
        "input": {"number": 5},
        "expected_output": {"answer": 120, "cached": False, "api_key": "key"}
    },
    {
        "test_id": "FACT-RETRIEVE-INVALID",
        "description": "Retrieve with negative number",
        "method": "POST",
        "endpoint": "/fact/retrieve",
        "headers": { "name": "key" },
        "input": {"number": -3},
        "expected_output": {"error": "422 Unprocessable Entity"}
    },
    {
        "test_id": "FACT-RETRIEVE-MISSING-AUTH",
        "description": "Retrieve without API key",
        "method": "POST",
        "endpoint": "/fact/retrieve",
        "headers": {},
        "input": {"number": 3},
        "expected_output": {"error": "403 Forbidden"}
    }
    ]
}

# Write to JSON file
json_output_path = Path(r"manual_test_cases.json")
with open(json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(test_cases, json_file, indent=4)

# Confirm saved
print(f"Created: {json_output_path}")
