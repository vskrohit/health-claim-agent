"""Project settings. They are read from the .env file in the project folder."""
import os
from dotenv import load_dotenv
# Read the .env file.
# override=True means: if Windows also has a variable with the same name,
# the value in .env wins. This avoids old keys causing confusing errors.

load_dotenv(override=True)

# Which model to use, written as "provider:model-name".
# If MODEL is missing or empty in .env, we use the default after "or".
MODEL = os.getenv("MODEL") or "groq:llama-3.3-70b-versatile"

def check_key() -> None:
    """Stop with a clear message if the API key for our provider is missing."""
    provider = MODEL.split(":", 1)[0] # "groq:llama..." -> "groq"
    key_name = f"{provider.upper()}_API_KEY" # -> "GROQ_API_KEY"
    if not os.getenv(key_name):
        raise SystemExit(f"{key_name} is missing. Add it to your .env file (Day 4, Step 3).")



