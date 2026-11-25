"""What a hospital bill looks like, written as Python data with rules."""
from datetime import date
from pydantic import BaseModel, Field,model_validator, ValidationError

class BillItem(BaseModel):
    """One line on the bill, for example 'Room rent (3 days) - Rs 9,000'."""
    description: str = Field(description="What was charged")
    amount: float = Field(ge=0, description="Amount in rupees. Never negative.")

class HospitalBill(BaseModel):
    """The main facts on a hospital bill."""
    patient_name: str = Field(description="Patient's full name")
    hospital_name: str = Field(description="Name of the hospital")
    admission_date: date = Field(description="Date the patient was admitted")
    discharge_date: date = Field(description="Date the patient went home")
    diagnosis: str = Field(description="Illness or reason for the stay")
    room_type: str | None = Field(default=None, description="Optional: type of room (e.g., 'Private', 'Semi-private')")
    items: list[BillItem] = Field(min_length=1, description="Every charge on the bill")
    total_amount: float = Field(ge=0, description="Final total in rupees")

    @model_validator(mode="after")
    def discharge_not_before_admission(self) -> "HospitalBill":
        if self.discharge_date < self.admission_date:
            raise ValueError("discharge_date is before admission_date")
        return self

    @model_validator(mode="after")
    def total_matches_items(self) -> "HospitalBill":
        items_total = sum(item.amount for item in self.items)
        if self.total_amount != items_total:
            raise ValueError(f"total_amount {self.total_amount} does not match sum of items {items_total}")
        return self 


if __name__ == "__main__":

    good_bill = {
    "patient_name": "Ravi Kumar",
    "hospital_name": "Shanti Care Hospital",
    "admission_date": "2026-08-12", # text is turned into a real date
    "discharge_date": "2026-08-15",
    "diagnosis": "Dengue fever",
    "room_type": "Private",
    "items": [{"description": "Room rent (3 days)", "amount": 9000}],
    "total_amount": 9000
    }

    # 1) A correct bill: Pydantic accepts it.

    bill = HospitalBill.model_validate(good_bill)
    days = (bill.discharge_date - bill.admission_date).days
    print("Good bill accepted. Days in hospital:", days)

    # 2) Two wrong bills. Each one has ONE mistake.

    wrong_dates = dict(good_bill, admission_date="2026-08-15", discharge_date="2026-08-12")
    negative_amount = dict(good_bill, items=[{"description": "Medicines", "amount": -500}])
    wrong_total = dict(good_bill, total_amount=8000)

    for name, data in [("Wrong dates", wrong_dates), ("Negative amount", negative_amount), ("Wrong total", wrong_total)]:
        try:
            HospitalBill.model_validate(data)
        except ValidationError as error:
            print(f"{name} -> rejected: {error.errors()[0]['msg']}")
