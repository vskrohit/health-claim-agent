"""The one place where we create the chat model.
The rest of the project calls get_llm() and never needs to know
which company (Groq, OpenAI, ...) is behind it.
"""
from langchain.chat_models import init_chat_model
from health_claim_agent.config import MODEL, check_key


def get_llm():
    check_key()
# temperature=0 -> the most predictable answers. We want facts, not creativity.
    return init_chat_model(MODEL, temperature=0)


if __name__ == "__main__":
    llm = get_llm()
    reply = llm.invoke("In one sentence, what does a health insurance claim checker do?")
    print("Model:", MODEL)
    print("Reply:", reply.content)
