# 🚀 AGI Idea Analyzer (Trueanalyser)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](#)

> **An Intelligent Framework for Real-Time Project Feasibility and Market Analysis.**

In the rapidly evolving landscape of technology and entrepreneurship, thousands of ideas are generated daily, yet many fail due to a lack of structured feasibility analysis or market grounding. **Trueanalyser** is a state-of-the-art AI-powered platform designed to provide instant, data-driven critiques of project ideas across 30+ diverse domains. By leveraging large language models (LLMs) and real-time web intelligence, it bridges the gap between raw concepts and actionable business intelligence.

---

## 📖 Table of Contents

- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Quick Start Configuration](#-quick-start-configuration)
- [API Reference](#-api-reference)
- [Demo Mode](#-demo-mode)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **Domain Support:** Analysis for 30+ domains including Engineering, Healthcare, Fintech, EdTech, and more.
- **Dynamic ML Scoring:** Provides multi-dimensional scoring assessing Feasibility, Innovation, Risk, Impact, and Complexity.
- **Budgetary Intelligence:** Outputs category-wise estimated costs (in USD) and realistic budget breakdowns based on current trends.
- **Temporal Analysis:** Estimates development phases and offers an implementation timeline.
- **AI Visuals:** Automated generation of project-themed imagery.
- **Demo Mode:** Fully functional using mock data for presentation purposes, eliminating API costs.

---

## 🏗 System Architecture

The platform is designed with a modern full-stack, decoupled architecture:

- **Frontend Layer:** React-based Single Page Application (SPA), built with Vite for optimal performance.
- **Backend API Layer:** FastAPI handles request routing, web analytics data, and AI model orchestration.
- **Intelligence Layer:**
  - *Baseline ML:* Scikit-Learn for initial domain-based complexity scoring (TF-IDF + Ridge Regression).
  - *Cognitive Engine:* Anthropic Claude API for nuanced interpretation, reasoning, and high-level synthesis.
  - *Search Engine:* DuckDuckGo API integration fetches real-time market data to ground LLM capabilities in facts.

**Data Flow:**  
`User Input` ➔ `Search Enrichment` ➔ `ML Scoring` ➔ `AI Synthesis` ➔ `Visual Analysis` ➔ `Final Report`

---

## 💻 Technology Stack

| Component | Technologies |
| :--- | :--- |
| **Frontend** | React.js, Tailwind CSS, Vite |
| **Backend** | Python 3.10+, FastAPI, Uvicorn, Pydantic |
| **Intelligence** | Scikit-learn, Anthropic API (Claude), DuckDuckGo Search API |

---

## 🚀 Quick Start Configuration

### Prerequisites
- **Node.js** 18+  
- **Python** 3.10+  

### Installation & Execution

#### 1. Frontend Setup
```bash
# Install dependencies
npm install

# Start the development server
npm run dev -- --host 0.0.0.0 --port 5173
```

#### 2. Backend Setup
We highly recommend utilizing a virtual environment for Python execution.
```bash
cd backend
python -m venv .venv
# Activate environment
source .venv/bin/activate    # On Linux/Mac
# .venv\Scripts\activate     # On Windows

# Install required Python packages
pip install -r requirements.txt

# Start backend server
npm run dev:api  # Alternatively: uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
```

#### 3. Environment Variables
Copy `.env.example` to `.env` in the root (create if missing):
```env
ANTHROPIC_API_KEY=your_key_here
```
*(Get the key from the Anthropic Console. Demo mode activates automatically without a key.)*

**Access Points:**
- **Frontend App:** [http://localhost:5173](http://localhost:5173)
- **FastAPI / Swagger API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Service health check |
| `GET` | `/api/fields` | Retrieve list of 30+ supported domains |
| `POST` | `/api/analyze` | Core endpoint: Analyze and score the submitted idea |
| `POST` | `/api/generate` | Generate random project ideas |

#### Analyze Endpoint (`/api/analyze`)

**Request Payload:**
```json
{
  "field": "Healthcare",
  "idea": "An AI platform that predicts patient readmission risk from EHR data and automates discharge planning."
}
```

---

## 🎮 Demo Mode

Demo Mode evaluates the system automatically using realistic mock data, ensuring developers and users can preview the deep-dive analysis (budgets, realistic scoring vectors, components, and project visuals) without connecting an active API Key. Perfect for portfolios and demonstrations.

---

## 🔮 Future Scope

- **User Authentication:** Implementing securely managed user accounts to save and track iterative project ideas.
- **Export Functionality:** Provide PDF/Docx output generation for compiled evaluation reports.
- **Collaboration Features:** Options for sharing analysis metrics with mentors and peers for actionable feedback.
- **Multi-Model Extensibility:** Integrating other enterprise LLMs (i.e., GPT-4, Gemini) to offer split-testing comparative analyses.

---

## 🤝 Contributing

We welcome community contributions.

1. Fork & clone the repository.
2. Install dependencies.
3. Switch to a new feature branch: `git checkout -b feature/your-feature-name`.
4. Commit your enhancements: `git commit -m "feat: Add newly integrated feature"`.
5. Push the changes to your remote branch.
6. Submit a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  <b>The Box Creations</b>
</div>
