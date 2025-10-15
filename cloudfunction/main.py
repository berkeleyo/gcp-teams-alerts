import os, json, functions_framework, urllib.request

TEAMS_WEBHOOK_URL = os.environ.get("TEAMS_WEBHOOK_URL", "")
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")  # optional simple auth

def make_card(title, severity, desc, link=None):
    return {
        "type": "message",
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.4",
                "body": [
                    {"type":"TextBlock","size":"Large","weight":"Bolder","text":title},
                    {"type":"TextBlock","text":f"Severity: {severity}"},
                    {"type":"TextBlock","wrap":True,"text":desc or "No description"}
                ],
                "actions":([{"type":"Action.OpenUrl","title":"Open in Cloud Console","url":link}] if link else [])
            }
        }]
    }

def post_to_teams(card):
    if not TEAMS_WEBHOOK_URL:
        raise RuntimeError("TEAMS_WEBHOOK_URL not set")
    req = urllib.request.Request(TEAMS_WEBHOOK_URL, data=json.dumps(card).encode(), headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()

@functions_framework.http
def alert_to_teams(request):
    if SECRET_TOKEN:
        if request.headers.get("X-Token") != SECRET_TOKEN:
            return ("unauthorized", 401)

    try:
        payload = request.get_json(silent=True) or {}
    except Exception:
        payload = {}

    incident = payload.get("incident", {})
    title = incident.get("policy_name", "GCP Monitoring Alert")
    sev = incident.get("severity", "N/A")
    url = incident.get("url")
    desc = incident.get("summary", "Alert notification")
    post_to_teams(make_card(title, sev, desc, url))
    return ("ok", 200)
