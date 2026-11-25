# Health Claim Agent
An AI agent that checks health insurance claims: it reads hospital documents,
pulls out the facts, checks them against the policy rules, and sends unclear
cases to a human reviewer with a clear summary.
> Work in progress. Built step by step over 14 weeks. This is week 2.
## What works today
- Sends a hospital bill to an AI model and gets back clean, structured data.
- Checks that data with rules (Pydantic): no negative amounts, and discharge
is never before admission.
- Works with any model provider through one setting in `.env`.
## Tech
Python 3.12, uv, LangChain, Pydantic, Groq.
## Run it
1. Install [uv](https://docs.astral.sh/uv/).
2. Get the code and install the packages:
```
    git clone https://github.com/vskrohit/health-claim-agent.git
    cd health-claim-agent
    uv sync

3. Copy `.env.example` to `.env` and put your own Groq API key in it.
4. Try it:
```
uv run python -m health_claim_agent.models
uv run python -m health_claim_agent.extract
```
## Project layout
```
data/samples/ made-up hospital bills for practice
src/health_claim_agent/
config.py reads settings from .env
llm.py creates the AI model in one place
models.py the shape and rules of a hospital bill
extract.py bill text in, checked data out
```
## Data
All bills in this project are made up. No real patient data is used.