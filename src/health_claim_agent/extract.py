from pathlib import Path
from health_claim_agent import llm
from health_claim_agent.llm import get_llm
from health_claim_agent.models import HospitalBill

# The project folder: extract.py -> health_claim_agent -> src -> project
PROJECT_DIR = Path(__file__).resolve().parents[2]

PROMPT = """You are a careful assistant at a health insurance company.
Read the hospital bill below and fill in every field.
Copy names and amounts exactly as written. Write dates as YYYY-MM-DD.
BILL:
{bill_text}
"""


def extract_bill(bill_text: str) -> HospitalBill:
# with_structured_output: the model must answer in the shape of HospitalBill.
    llm = get_llm().with_structured_output(HospitalBill)
    return llm.invoke(PROMPT.format(bill_text=bill_text))

if __name__ == "__main__":
    bill_file = PROJECT_DIR / "data" / "samples" / "bill_001.txt"
    bill = extract_bill(bill_file.read_text(encoding="utf-8"))
    print(bill.model_dump_json(indent=2))
    print("Type of admission_date:", type(bill.admission_date).__name__)
    print("Items add up to:", sum(item.amount for item in bill.items))