from pydantic import BaseModel

class Customer(BaseModel):
    total_day_minutes: float
    total_day_charge: float
    number_customer_service_calls: int
    avg_call_duration: float
    number_vmail_messages: int
    total_intl_calls: int
    avg_cost_per_minute: float
    total_eve_minutes: float
    total_eve_charge: float
    phone_number: float