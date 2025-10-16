![CI](https://github.com/berkeleyo/gcp-teams-alerts/actions/workflows/python-ci.yml/badge.svg)
![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# GCP -> Teams Alerts (Cloud Functions)

**Flow:** Cloud Monitoring â†’ Webhook Notification Channel â†’ **HTTP Cloud Function** â†’ Teams Incoming Webhook.

## Deploy
```bash
cd gcp-teams-alerts
export TEAMS_WEBHOOK_URL="https://outlook.office.com/webhook/..."
export SECRET_TOKEN="optional-shared-secret"
bash scripts/deploy.sh
```

## Wire Monitoring
- Create a **notification channel** of type **Webhook** pointing to the function URL.  
- (Optional) Send header `X-Token: <SECRET_TOKEN>` in the webhook channel for basic auth.

