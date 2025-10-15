# GCP -> Teams Alerts (Cloud Functions)

**Flow:** Cloud Monitoring → Webhook Notification Channel → **HTTP Cloud Function** → Teams Incoming Webhook.

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
