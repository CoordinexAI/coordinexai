# 🌀 CoordinexAI

> Detect the friction before it becomes failure.

**The Friction Constant** is the silent drag that slows down teams:  
missed handoffs, delays, vague tasks, and “just checking in” loops.

**CoordinexAI** detects that drag before it snowballs—giving you the nudges and insights you didn’t know you needed.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://coordinexai.streamlit.app)

---

## 🛠 What It Does

- Connects to Slack  
- Analyzes conversations for delays, vagueness, and dropped threads  
- Scores threads using a Friction Index  
- Surfaces coordination breakdowns with clear prompts  

---

## 🧪 Try It Free

🔗 **Launch App**: [https://coordinexai.streamlit.app](https://coordinexai.streamlit.app)

📩 **Request a Friction Report** (no login):  
[https://tally.so/r/nO1EXX](https://tally.so/r/nO1EXX) ← *(replace this with your actual Tally form link)*

---

## 💡 Use Cases

- Founders managing async teams  
- Chiefs of Staff tracking execution  
- Project Managers identifying blockers  
- Ops teams cleaning up coordination chaos  

---

## 📌 Built With

- Python · Streamlit · Slack API · GPT · GitHub  

> _“If you can’t see your friction, you can’t fix your flow.”_

---


## Running the Agents

```powershell
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt

# Terminals:
.\.venv\Scripts\python.exe -m agents.ingestor_agent.main
.\.venv\Scripts\python.exe -m agents.analytics_agent.main
\.venv\Scripts\python.exe -m backend.main
\.venv\Scripts\streamlit.exe run app/main.py
```

