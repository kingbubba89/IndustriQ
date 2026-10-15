from datetime import datetime, timedelta, timezone
from random import Random
from math import exp

from industriq.config import EquipmentConfig
from industriq.readings import EquipmentReading


def simulate_fan(
    equipment: EquipmentConfig,
    duration_s: int = 600,
    sampling_interval_s: int = 1,
    seed: int = 42,
) -> list[EquipmentReading]:
    if duration_s <= 0 or sampling_interval_s <= 0:
        raise ValueError("Duration and sampling interval must be positive.")

    rng = Random(seed)
    start_time = datetime(2026, 1, 1, tzinfo=timezone.utc)

    frequency_hz = equipment.max_frequency_hz * 0.8
    speed_ratio = frequency_hz / equipment.motor.rated_frequency_hz

    # Simplified demonstration model, not a calibrated motor model.
    expected_current_a = equipment.motor.full_load_current_a * (
        0.25 + 0.65 * speed_ratio**2
    )

    temperature_c = equipment.ambient_temperature_c
    target_temperature_c = equipment.ambient_temperature_c + (
        40.0 * (
            expected_current_a / equipment.motor.full_load_current_a
        ) ** 2
    )

    # Fraction of the temperature gap closed during each sampling interval.
    thermal_response = 1.0 - exp(-sampling_interval_s / 300.0)

    readings = []

    for elapsed_s in range(0, duration_s, sampling_interval_s):
        temperature_c += (
            target_temperature_c - temperature_c
        ) * thermal_response

        reading = EquipmentReading(
            timestamp=start_time + timedelta(seconds=elapsed_s),
            equipment_id=equipment.equipment_id,
            run_state="RUNNING",
            current_a=round(
                max(0.0, expected_current_a + rng.gauss(0.0, 0.5)),
                2,
            ),
            frequency_hz=round(frequency_hz, 2),
            motor_temperature_c=round(temperature_c, 2),
            load_demand_pct=80.0,
            speed_feedback_rpm=round(
                equipment.motor.rated_speed_rpm * speed_ratio,
                1,
            ),
        )

        readings.append(reading)

    return readings