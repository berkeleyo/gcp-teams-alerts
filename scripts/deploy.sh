#!/usr/bin/env bash
set -euo pipefail

REGION=${REGION:-"europe-west2"}
NAME=${NAME:-"alert-to-teams"}
WEBHOOK=${TEAMS_WEBHOOK_URL:-""}
TOKEN=${SECRET_TOKEN:-""}

if [ -z "$WEBHOOK" ]; then
  echo "Set TEAMS_WEBHOOK_URL env var"; exit 1
fi

gcloud functions deploy "$NAME" \
  --gen2 \
  --region "$REGION" \
  --runtime python311 \
  --source ./cloudfunction \
  --entry-point alert_to_teams \
  --trigger-http \
  --set-env-vars TEAMS_WEBHOOK_URL="$WEBHOOK",SECRET_TOKEN="$TOKEN" \
  --allow-unauthenticated
