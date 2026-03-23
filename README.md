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

### Problem Statement
Everyday life is filled with repetitive micro-tasks: planning the day, organizing schedules, generating meals, creating shopping lists, drafting emails, and remembering personal preferences spread across different apps.
Although these tasks seem small, they collectively consume 5–10 hours every week, adding cognitive load and reducing productivity.

People need a personal assistant, but not everyone can hire one.
We need a scalable, personalized, AI-driven solution that helps individuals manage and automate their daily routines effortlessly.

This problem is important because:

It affects everyone—students, professionals, parents, remote workers.

It impacts productivity, focus, and mental well-being.

It is perfect for AI systems that excel at organization, planning, and language tasks.

### Why agents?
A single model can generate text, but life management requires specialization:

->Planning a daily schedule

->Drafting professional emails

->Generating meal plans

->Building shopping lists

->Scheduling events

->Remembering personal preferences over time

Instead of one giant model doing everything, agents provide:

1. Modularity — Each agent focuses on one task (planner, meal agent, email agent, calendar agent).

2. Coordination — The orchestrator routes user requests to the right specialist.

3. Memory — Agents maintain session memory and long-term preference storage.

4. Scalability — Easy to add more agents later.

5. Interpretability — You can see which agent handled what.

Agents work the same way a real assistant team works:
specialized roles → collaboration → personalized output.

This makes agents the ideal solution for a personal executive assistant.

### What you created 
LifeFlow is a multi-agent personal concierge system built in Python and powered by Gemini.

Agents

-> Planner Agent → creates structured daily/weekly plans

-> Meal Agent → generates 3-day meals + ingredients

-> Email Agent → drafts professional emails on request

-> Calendar Agent → schedules events automatically

-> Orchestrator Agent → routes user requests to the right specialist

Tools

-> Shopping Tool → converts meals → smart shopping list

-> Calendar Tool → schedules events

-> Search Tool → external info lookup (for future expansion)

Memory System

-> SessionMemory → short-term state

-> LongTermMemory → stores preferences (diet, work hours, routine)

Observability

-> Unified logging for every agent interaction.

### Demo (How LifeFlow Behaves)

User:
-> “Plan my day tomorrow.”

LifeFlow:

-> PlannerAgent generates a structured schedule

-> Uses long-term memory (work hours, habits)

-> Returns an 8am–6pm optimized plan

User:
-> “I need a 3-day high-protein meal plan.”

LifeFlow:

-> MealAgent creates meal suggestions

-> Ingredients extracted

-> ShoppingTool generates a shopping list

User:
-> “Draft an email to follow up on the project status.”

LifeFlow:

-> EmailAgent writes a clear, professional email

User:
-> “Schedule a team sync on Thursday.”

LifeFlow:

-> CalendarAgent uses CalendarTool

-> Adds event and returns confirmation

### The Build (Technologies Used)
Languages & Frameworks

-> Python (Kaggle + Cloud Run ready)

-> Google Gemini 2.0 Flash (LLM backbone)

Agents & Architecture

-> Multi-agent system (sequential + parallel flows)

-> Orchestrator-driven routing

-> Specialized sub-agents

Tools

-> Custom Shopping Tool

-> Calendar Tool

-> Search Tool

-> Code execution for utility tasks

Memory

-> JSON-based long-term memory

-> In-memory session state

Observability

-> Centralized logging interface

### If I had more time, this is what I'd do
If I were to continue expanding LifeFlow, I would add:

1. Voice Interaction Layer

Hands-free use via speech input + TTS output.

2. Auto-Execution Mode

Agents that not only plan tasks but take action—sending emails, booking reservations, creating real calendar events.

3. Daily Reflection + Analytics

A journaling + habit tracking agent that analyzes your routines and suggests optimization.

4. Real Shopping Integrations

Actual integration with Amazon Fresh, Walmart, or Instacart.

5. Smart Context Compaction

More efficient long-term state management for multi-week personalization.

6. Mobile App or Chat Interface

A simple UI for everyday use beyond notebook.
