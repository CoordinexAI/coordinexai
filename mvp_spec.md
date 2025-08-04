# CoordinexAI MVP Specification

## Goal
To develop an intelligent agent that detects and reduces coordination friction within digital teams.

## Features

### 1. Friction Detection
- Analyze communication threads for:
  - Delayed replies
  - Repeated nudges
  - Vague task definitions
  - Hand-off failures

### 2. Friction Score Engine
- Track metrics such as:
  - Avg time to response
  - # of follow-ups
  - % of unanswered requests
  - # of clarification loops

### 3. AI Nudging System
- Examples:
  - “You’ve asked twice — want me to escalate?”
  - “Still waiting on feedback from 2/4 people.”
  - “This thread is stalled. Want me to summarize and propose next steps?”

## Integrations
- Slack (or Discord) for communication logs
- Notion or Asana for task tracking
- Google Calendar for scheduling gaps

## Architecture Sketch
- Agent layer (LangChain or AutoGPT style)
- Communication APIs
- Friction Scoring Logic
- Lightweight analytics UI

## Milestones
- [ ] MVP prototype with dummy data
- [ ] Internal pilot
- [ ] Real-time Slack integration
- [ ] Launch dashboard

