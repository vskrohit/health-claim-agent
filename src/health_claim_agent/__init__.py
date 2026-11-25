def main() -> None:
    print("Health Claim Agent is ready!")
    print("Try these commands:")
    print(" uv run python -m health_claim_agent.models # check sample bills (no AI)")
    print(" uv run python -m health_claim_agent.llm # one question to the AI")
    print(" uv run python -m health_claim_agent.extract # the AI reads bill_001.txt")