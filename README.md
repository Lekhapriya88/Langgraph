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
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

3. Run the script:
   ```bash
   python langgraph_agent_with_logging.py
   ```

## 📝 Example Output

```
🔍 Processing Ticket: P001 - User cannot connect to VPN
✅ Action: Troubleshoot VPN connection issue
📝 Notes: User unable to connect to VPN. Escalated to support team.

📊 Final Results:
  Ticket_ID           Action                  Notes
  ...                 ...                     ...
```
