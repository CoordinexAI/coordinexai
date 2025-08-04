import streamlit as st
import datetime
from slack_sdk import WebClient

st.title("CoordinexAI: Friction Detector with Slack")

SLACK_TOKEN = st.secrets["SLACK_TOKEN"]
CHANNEL_ID = st.text_input("Slack Channel ID", "")

client = WebClient(token=SLACK_TOKEN)

def fetch_slack_messages(channel_id):
    try:
        response = client.conversations_history(channel=channel_id, limit=50)
        messages = [
            {"sender": msg.get("user", "bot"), "content": msg["text"], "timestamp": datetime.datetime.fromtimestamp(float(msg["ts"]))}
            for msg in response["messages"]
        ]
        return messages
    except Exception as e:
        st.error(f"Slack fetch failed: {e}")
        return []

def analyze_thread(thread):
    friction_score = 0
    response_times = []
    repeats = 0
    vague_requests = 0

    for i in range(1, len(thread)):
        delta = (thread[i]['timestamp'] - thread[i-1]['timestamp']).total_seconds() / 3600
        if delta > 24:
            friction_score += 1
            response_times.append(round(delta, 2))

    for msg in thread:
        if "just checking in" in msg['content'].lower():
            repeats += 1
        if "can you handle this" in msg['content'].lower():
            vague_requests += 1

    friction_score += repeats + vague_requests

    return {
        "response_delays": response_times,
        "follow_ups": repeats,
        "vague_requests": vague_requests,
        "friction_score": friction_score
    }

if CHANNEL_ID:
    thread = fetch_slack_messages(CHANNEL_ID)
    if thread:
        st.markdown("### Slack Thread")
        for msg in thread:
            st.write(f"[{msg['timestamp']}] {msg['sender']}: {msg['content']}")

        st.markdown("### Friction Analysis")
        results = analyze_thread(thread)
        st.write(f"Response delays (hrs): {results['response_delays']}")
        st.write(f"Follow-up messages: {results['follow_ups']}")
        st.write(f"Vague requests: {results['vague_requests']}")
        st.write(f"**Friction Score**: {results['friction_score']}")
