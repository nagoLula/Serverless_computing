import logging
import json
import azure.functions as func # pyright: ignore[reportMissingImports]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing potassium classification request.")

    try:
        req_body = req.get_json()
        potassium = req_body.get("potassium")

        if potassium is None:
            return func.HttpResponse(
                json.dumps({"error": "'potassium' is required."}),
                status_code=400,
                mimetype="application/json"
            )

        if not isinstance(potassium, (int, float)):
            return func.HttpResponse(
                json.dumps({"error": "'potassium' must be a number."}),
                status_code=400,
                mimetype="application/json"
            )

        if 3.5 <= potassium <= 5.0:
            status = "normal"
            category = "Normal (3.5–5.0 mmol/L)"
        else:
            status = "abnormal"
            category = "Abnormal (<3.5 or >5.0 mmol/L)"

        return func.HttpResponse(
            json.dumps({
                "potassium": potassium,
                "status": status,
                "category": category
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


