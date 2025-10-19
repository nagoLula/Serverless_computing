import urllib.request
import json

url = "https://your-azure-endpoint-url"  # Replace with your actual Azure URL
payload = {"potassium": 4.1}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        resp_text = resp.read().decode("utf-8")
        try:
            resp_json = json.loads(resp_text)
        except json.JSONDecodeError:
            resp_json = {"raw_response": resp_text}
        print("Azure Response:", resp_json)
except urllib.error.URLError as e:
    print("Request failed:", e)


