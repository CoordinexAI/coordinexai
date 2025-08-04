# CoordinexAI

An AI-powered Streamlit app that detects coordination friction in team communications. Now supports real Slack integration.

## Features
- Pulls Slack message threads via API
- Analyzes for delays, vague requests, and repeated nudges
- Outputs a friction score

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## Secrets Configuration
Store your Slack Bot Token in `.streamlit/secrets.toml`:
```toml
SLACK_TOKEN = "xoxb-your-token"
```

## Deployment
Push to GitHub and deploy via [Streamlit Cloud](https://share.streamlit.io).
