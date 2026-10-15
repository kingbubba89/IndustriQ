from dataclasses import dataclass

@dataclass(frozen=True)
class MotorSpecs:
    horsepower: float
    rated_voltage_v: float
    full_load_current_a: float
    rated_speed_rpm: float
    rated_frequency_hz: float
    frame: str | None = None


@dataclass(frozen=True)
class EquipmentConfig:
    equipment_id: str
    name: str
    motor: MotorSpecs
    max_frequency_hz: float
    ambient_temperature_c: float
    current_warning_a: float
    current_critical_a: float
    temperature_warning_c: float
    temperature_critical_c: float
    alert_persistence_s: int
    speed_feedback_source: str = "drive_estimated"
