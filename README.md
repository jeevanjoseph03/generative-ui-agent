#  Generative UI Agent

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Tech Stack](https://img.shields.io/badge/tech-FastAPI%20%7C%20Next.js%20%7C%20Groq-blueviolet)

> **"Don't just describe the dashboard. Build it."**

This project is an experimental **Agentic AI System** that generates fully functional, interactive React UI components from natural language prompts in real-time. It bridges the gap between **LLM Reasoning** (Backend) and **Dynamic Rendering** (Frontend).

## 🏗 Architecture

The system follows a strict **Schema-First** approach to prevent hallucinations:

`User Prompt` → `FastAPI` → `Llama 3 (Groq)` → `Pydantic Validation` → `JSON Schema` → `Next.js Dynamic Renderer`

##  Features

- **⚡ Instant Generation:** Uses Groq's LPU inference engine for <1s latency.
- **🛡️ Type-Safe AI:** Enforced strict JSON schemas using Pydantic.
- **🎨 Generative UI:** React components are chosen and rendered on the fly based on data type.
- **✨ Animated Interactions:** Smooth Framer Motion transitions for a "magic" feel.

##  Quick Start

### Backend (The Brain)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```

### Frontend (The Face)
```bash
cd frontend
npm install
npm run dev
```

## 🛠️ Tech Stack
**Backend:** Python, FastAPI, Pydantic, OpenAI SDK

**AI Model:** Llama 3.1 70B (via Groq)

**Frontend:** Next.js 14, TypeScript, Tailwind CSS

**Visualization:** Recharts, Framer Motion

## 🤝 Contributing
This is a proof-of-concept for A2UI (Agent-to-UI) protocols. Issues and PRs are welcome!