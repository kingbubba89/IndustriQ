from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class EquipmentReading:
    timestamp: datetime
    equipment_id: str
    run_state: str
    current_a: float
    frequency_hz: float
    motor_temperature_c: float
    load_demand_pct: float
    actual_speed_rpm: float | None = None