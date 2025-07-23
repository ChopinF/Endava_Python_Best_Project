# Manual Testing Plan – Math Microservice

This document defines manual test scenarios for verifying the core API endpoints based on the provided Postman collection.

---

## Endpoint: `POST /pow/int`, `/pow/float`, `/pow/complex`

| Test ID | Description        | Endpoint       | Input                       | Expected Output | Notes                 |
| ------- | ------------------ | -------------- | --------------------------- | --------------- | --------------------- |
| POW-01  | Integer power      | `/pow/int`     | `{ "a": 2, "b": 3 }`        | result = 8      | Basic integer power   |
| POW-02  | Float power        | `/pow/float`   | `{ "a": 4, "b": 0.5 }`      | result = 2.0    | Square root           |
| POW-03  | Complex number     | `/pow/complex` | `{ "a": "1+1j", "b": "2" }` | complex result  | Handle complex values |
| POW-04  | Invalid data types | `/pow/int`     | `{ "a": "a", "b": "b" }`    | 400 Bad Request | Input validation      |

---

## Endpoint: `POST /fibo/retrieve`

| Test ID | Description           | Input              | Expected Output        | Notes                  |
| ------- | --------------------- | ------------------ | ---------------------- | ---------------------- |
| FIB-01  | 10th Fibonacci number | `{ "number": 10 }` | result = 55            | Correct result         |
| FIB-02  | 0th Fibonacci number  | `{ "number": 0 }`  | result = 0             | Edge case              |
| FIB-03  | Negative input        | `{ "number": -1 }` | 422 / validation error | Should reject          |
| FIB-04  | Missing auth header   | `{ "number": 4 }`  | 403 / unauthorized     | Authorization required |

---

## Endpoint: `POST /fact/retrieve`

| Test ID | Description         | Input               | Expected Output        | Notes                  |
| ------- | ------------------- | ------------------- | ---------------------- | ---------------------- |
| FAC-01  | Factorial of 5      | `{ "number": 5 }`   | result = 120           | Valid input            |
| FAC-02  | Factorial of 0      | `{ "number": 0 }`   | result = 1             | Edge case              |
| FAC-03  | Large input         | `{ "number": 100 }` | result = large number  | Stress test            |
| FAC-04  | Negative input      | `{ "number": -5 }`  | 422 / validation error | Should reject          |
| FAC-05  | Missing auth header | `{ "number": 3 }`   | 403 / unauthorized     | Authorization required |

---

## Additional Notes

* All endpoints require JSON payloads.
* Most endpoints expect a `name: key` header; test cases are included to verify behavior with and without it.
* Redis caching may impact response time for repeated Fibonacci or factorial queries.
* Authorization handling should be tested thoroughly across all endpoints.
