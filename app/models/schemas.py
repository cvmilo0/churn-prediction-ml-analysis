from pydantic import BaseModel

class Customer(BaseModel):
    total_day_charge: float
    total_day_minutes: float
    avg_call_duration: float
    number_customer_service_calls: int
    number_vmail_messages: int
    total_intl_calls: int
    total_eve_charge: float
    avg_cost_per_minute: float
    total_eve_minutes: float
    phone_number: float
    state: str
    total_intl_charge: float
    total_intl_minutes: float
    intl_usage_ratio: float
    area_code: float
    total_night_minutes: float
    total_night_charge: float
    total_calls: int
    high_service_usage_3: bool
    total_day_calls: int