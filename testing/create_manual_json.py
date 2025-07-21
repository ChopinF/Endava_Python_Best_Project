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
    ]
}

# Write to JSON file
json_output_path = Path(r"testing\manual_test_cases.json")
with open(json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(test_cases, json_file, indent=4)

# Confirm saved
print(f"Created: {json_output_path}")
