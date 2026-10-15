from industriq.readings import EquipmentReading


def print_reading(title: str, reading: EquipmentReading) -> None:
    speed = (
        f"{reading.speed_feedback_rpm:.1f} RPM"
        if reading.speed_feedback_rpm is not None
        else "Unavailable"
    )

    print(f"\n{title}")
    print("-" * 44)
    print(f"{'Equipment:':<20}{reading.equipment_id}")
    print(f"{'Timestamp:':<20}{reading.timestamp:%Y-%m-%d %H:%M:%S %Z}")
    print(f"{'State:':<20}{reading.run_state}")
    print(f"{'Current:':<20}{reading.current_a:.2f} A")
    print(f"{'Frequency:':<20}{reading.frequency_hz:.1f} Hz")
    print(f"{'Motor temperature:':<20}{reading.motor_temperature_c:.2f} °C")
    print(f"{'Load demand:':<20}{reading.load_demand_pct:.1f} %")
    print(f"{'Speed feedback:':<20}{speed}")