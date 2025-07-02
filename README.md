# LangGraph Prebuilt Agent for ITSM Tickets

This repository contains a simple example using LangGraph's `create_react_agent` to process synthetic IT support tickets.

## 🔍 Use Case

The script simulates triage automation for ITSM tickets, helping determine whether to **resolve** or **escalate** based on the summary text.

### Features:
- Uses LangGraph’s prebuilt agent with tools and hooks
- Defines structured responses using Pydantic
- Supports synthetic ticket flow simulation
- Prints step-by-step results to console

## 📂 Files

- `langgraph_agent_with_logging.py`: The main Python script with all logic and logging.

## ⚙️ Setup

1. Install required packages:
   ```bash
   pip install langgraph langchain-openai pydantic pandas
