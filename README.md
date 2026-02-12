# AI Multi-Agent Stock Intelligence & Investment Research System

## Overview
This project implements a hierarchical multi-agent artificial intelligence system for automated financial research and investment intelligence using the CrewAI framework.  
The system identifies trending companies in the financial news, performs structured financial research, and produces an informed investment recommendation supported by analysis and real-time notification capabilities.

It demonstrates a production-oriented agent architecture that integrates information retrieval, reasoning, decision synthesis, and automated user communication within a coordinated multi-agent workflow.

This repository showcases the design and implementation of autonomous financial research agents capable of collaborating to support data-driven investment exploration.

---

## Key Features
- Multi-agent hierarchical architecture using CrewAI  
- Automated discovery of trending companies from financial news  
- Structured financial research and market analysis  
- Investment candidate evaluation and selection  
- Real-time push notification delivery to users  
- Modular agent and task configuration  
- Pydantic-based structured outputs for reliability and traceability  
- Tool-integrated agents for external data retrieval and communication  

---

## System Architecture

### Agent Hierarchy
The system is organized using a hierarchical coordination model in which a manager agent orchestrates task delegation and workflow execution.
```
Manager Agent (Coordinator)
│
├── Trending Company Finder (News Intelligence)
│       ↓
├── Financial Researcher (Deep Company Analysis)
│       ↓
└── Stock Picker (Investment Decision + Notification)
```
### Agent Roles

#### Manager
Coordinates the workflow, delegates tasks across agents, and ensures that the system produces a coherent and logically consistent investment decision.

#### Trending Company Finder
Identifies trending companies within a specified sector by analyzing recent financial and market news. Ensures discovery of new and relevant companies for further evaluation.

#### Financial Researcher
Performs comprehensive financial and strategic analysis of trending companies. Produces structured insights on market position, competitive landscape, growth outlook, and investment potential.

#### Stock Picker
Synthesizes research findings and selects the most promising investment candidate. Generates a final investment rationale and sends a real-time notification to the user.

---

## Workflow

1. **Trending Discovery**  
   The system scans recent financial news and identifies emerging companies attracting market attention.

2. **Company Research**  
   Each company is analyzed in depth to evaluate strategic position, financial strength, and growth outlook.

3. **Investment Selection**  
   The stock picker evaluates research outputs and selects the strongest candidate.

4. **User Notification**  
   A push notification is sent to the user with the selected company and key rationale.

5. **Detailed Report Generation**  
   A comprehensive decision report is produced and stored.

---

## Technology Stack

- Python 3.10+
- CrewAI (multi-agent orchestration framework)
- CrewAI Tools (search and external integrations)
- Serper API (financial/news search)
- Pydantic (structured outputs and validation)
- Pushover API (real-time notifications)

---

## Project Structure
```
stock_advisor/
│
├── src/stock_advisor/
│   ├── crew.py                # Crew and agent definitions
│   ├── main.py                # Execution entry point
│   ├── tools/
│   │   └── push_tool.py       # Push notification tool
│   └── config/
│       ├── agents.yaml        # Agent definitions
│       └── tasks.yaml         # Task workflow definitions
│
├── output/                    # Generated reports and decisions
├── .env                       # API keys and environment variables
├── pyproject.toml             # Project configuration
└── README.md
```
---

## Installation

Ensure Python version between 3.10 and 3.13.

Install dependencies using UV or pip:

```bash
pip install uv
uv sync
```
---

## **Environment Variables**

OPENAI_API_KEY=your_openai_key<br>
SERPER_API_KEY=your_serper_key<br>
PUSHOVER_USER=your_pushover_user<br>
PUSHOVER_TOKEN=your_pushover_token<br>

---

## Running the System
Execute the multi-agent workflow:<br>
```
crewai run
```
---

## Author

**Faria Jaheen, PhD.**  
AI Researcher & Engineer specializing in next-generation intelligent systems.

**Specializing in:**
<br>
	-	Multi-agent AI systems<br>
	-	Generative AI engineering<br>
	-	Autonomous software systems<br>
	-	Intelligent developer tooling<br>
