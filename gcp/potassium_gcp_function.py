import json

def classify_potassium(request):
    try:
        request_json = request.get_json()
        potassium = request_json.get("potassium")

        if potassium is None:
            return json.dumps({"error": "'potassium' is required."}), 400

        if not isinstance(potassium, (int, float)):
            return json.dumps({"error": "'potassium' must be a number."}), 400

        if 3.5 <= potassium <= 5.0:
            status = "normal"
            category = "Normal (3.5–5.0 mmol/L)"
        else:
            status = "abnormal"
            category = "Abnormal (<3.5 or >5.0 mmol/L)"

        return json.dumps({
            "potassium": potassium,
            "status": status,
            "category": category
        }), 200

    except Exception as e:
        return json.dumps({"error": str(e)}), 500


