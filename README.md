# Serverless_computing
A multi-cloud serverless deployment project for classifying serum potassium levels using HTTP-triggered functions in Google Cloud and Azure.

----

## Repository Structure

504_serverless_functions/ ├ azure/ │  ├ test_azure.py │   └ potassium_azure_function/ │    ├ init.py │      ├ function.json │      └ screenshots/ ├ gcp/ │  ├ potassium_gcp_function.py │   ├ test_gcp.py │   └ screenshots/ ├ LICENSE ├ README.md ├ .gitignore ├ requirements.txt

## Function Overview

| Cloud | File | Trigger | Input | Output |
|-------|------|---------|-------|--------|
| GCP   | `potassium_gcp_function.py` | HTTP | JSON with `"potassium"` | JSON with `"classification"` |
| Azure | `__init__.py` + `function.json` | HTTP | JSON with `"potassium"` | JSON with `"classification"` |

---

## Deployment Screenshots

### GCP
- Function deployed with public URL  
  -  POST test result: `"abnormal"`  
-  Logs showing successful execution

### Azure
- Function deployed with public URL  
  -   POST test result: `"normal"`  
- Logs showing successful execution

_Screenshots are located in the respective `screenshots/` folders._

---

##  Testing Scripts

- `test_gcp.py` and `test_azure.py` use Python’s `requests` library to send POST requests and print responses.
- Sample input:
  ```json
  { "potassium": 5.2 }

