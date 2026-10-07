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

FAN_CONFIG = EquipmentConfig(
    equipment_id="FAN_001",
    name="Cement Plant Process Fan",
    motor=MotorSpecs(
    horsepower=100.0,
    rated_voltage_v=460.0,
    full_load_current_a=100.0,
    rated_speed_rpm=1780.0,
    rated_frequency_hz=60.0,
),
    max_frequency_hz=60.0,
    ambient_temperature_c=25.0,
    current_warning_a=105.0,
    current_critical_a=115.0,
    temperature_warning_c=90.0,
    temperature_critical_c=110.0,
    alert_persistence_s=30,
)