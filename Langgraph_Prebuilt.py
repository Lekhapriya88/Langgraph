# Updated script with corrected docstring and step-by-step print statements
import os
import pandas as pd
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# Set your OpenAI API key as an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("Please set the OPENAI_API_KEY environment variable")

# Tool definition
def kb_lookup(query: str) -> str:
    if "disk" in query.lower():
        return "Refer to KB article 'disk' for instructions on resolving disk space issues."
    return "Troubleshoot: escalate to appropriate support team."

# Hooks
def pre_hook(state, config): return state
def post_hook(state, config): return state

# Pydantic response model
class TicketResponse(BaseModel):
    action: str
    notes: str

# Instantiate model and agent
model = ChatOpenAI(model="gpt-3.5-turbo")
agent = create_react_agent(
    model=model,
    tools=[kb_lookup],
    pre_model_hook=pre_hook,
    post_model_hook=post_hook,
    response_format=TicketResponse
)

# Sample synthetic tickets
tickets = [
    {"Ticket_ID": "P001", "Summary": "User cannot connect to VPN"},
    {"Ticket_ID": "P002", "Summary": "Disk space issue on shared server"},
    {"Ticket_ID": "P003", "Summary": "Printer not responding"},
]

# Run agent and collect results with logs
results = []
for ticket in tickets:
    print(f"\\n Processing Ticket: {ticket['Ticket_ID']} - {ticket['Summary']}")
    try:
        response = agent.invoke({"messages": [{"role": "user", "content": ticket["Summary"]}]})
        structured = response["structured_response"]
        print(f"Action: {structured.action}")
        print(f"Notes: {structured.notes}")
        results.append({
            "Ticket_ID": ticket["Ticket_ID"],
            "Action": structured.action,
            "Notes": structured.notes
        })
    except Exception as e:
        print(f" Error: {str(e)}")
        results.append({
            "Ticket_ID": ticket["Ticket_ID"],
            "Action": "error",
            "Notes": str(e)
        })

# Convert results to DataFrame
df = pd.DataFrame(results)
print("\\n Final Results:")
print(df)
"""

Save to new .py file
updated_script_path = Path("/mnt/data/langgraph_agent_with_logging.py")
updated_script_path.write_text(updated_script_content)




