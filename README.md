# 🌟 LifeFlow — AI Personal Executive Assistant

LifeFlow is a multi-agent concierge system that automates daily planning, meal generation, email drafting, and scheduling.  
Built as part of the **Google + Kaggle AI Agents Intensive (Nov 2025)**.

---

## 🚀 Features

- Multi-agent architecture (planner, meal agent, email agent, calendar agent)
- Sequential + parallel orchestration
- Gemini-powered LLM agents
- Custom MCP-style tools
- Memory (session + long-term)
- Logging & observability
- Ready for Cloud Run deployment

---

## 🧠 Architecture

```
Orchestrator Agent
       │
       ├── PlannerAgent
       ├── MealAgent
       ├── EmailAgent
       └── CalendarAgent
       │
 Tools → Search, Calendar API, Meal DB
 Memory → Session + Long-term preferences
```

---

## 🛠 Setup

```bash
pip install google-genai
```

Run:

```bash
python main.py
```

---

## 📦 Code Structure

- `agents/` — all sub-agents  
- `tools/` — custom tools  
- `memory/` — session + persistent memory  
- `utils/` — logger  
- `main.py` — entrypoint  

---

## 📹 Video Components

Your 3-minute demo should cover:
- Problem
- Why agents
- Architecture diagram
- Demo of all 4 tasks
- Tools used
- What you learned

---

## 🏆 Evaluation Coverage

- Multi-agent system ✔  
- Tools (custom + built-in) ✔  
- Memory (session + long term) ✔  
- Observability ✔  
- Context engineering ✔  
- Deployable ✔  
