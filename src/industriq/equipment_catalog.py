from industriq.config import EquipmentConfig, MotorSpecs

# Assumed equipment specifications for simulation.
# Not verified plant nameplates or protection settings.

STACK_FAN_CONFIG = EquipmentConfig(
    equipment_id="Stack_Fan_k1",
    name="K1 Stack Fan",
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
    speed_feedback_source= "drive_estimated"
)

# Kiln Main Drive
KILN_MAIN_DRIVE_CONFIG = EquipmentConfig(
    equipment_id="Kiln_Main_Drive_K1",
    name="Kiln Main Drive Motor",
    motor=MotorSpecs(
        horsepower=1000.0,
        rated_voltage_v=480.0,
        full_load_current_a=550.0,
        rated_speed_rpm=1785.0,
        rated_frequency_hz=60.0,
        frame="5010S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=45.0,  # hot environment near kiln
    current_warning_a=550.0,
    current_critical_a=575.0,
    temperature_warning_c=100.0,
    temperature_critical_c=120.0,
    alert_persistence_s=15,
    speed_feedback_source="encoder"
)

# Kiln ID Fan - induced draft fan pulling gases through kiln
KILN_ID_FAN_CONFIG = EquipmentConfig(
    equipment_id="Kiln_ID_Fan_K1",
    name="Kiln Induced Draft Fan",
    motor=MotorSpecs(
        horsepower=250.0,
        rated_voltage_v=4160.0,
        full_load_current_a=100.0,
        rated_speed_rpm=1785.0,
        rated_frequency_hz=60.0,
        frame="4510S"
    ),
    max_frequency_hz=58.0,  # rarely runs at full speed
    ambient_temperature_c=40.0,
    current_warning_a=105.0,
    current_critical_a=115.0,
    temperature_warning_c=95.0,
    temperature_critical_c=115.0,
    alert_persistence_s=20,
    speed_feedback_source="drive_estimated"
)

# Raw Mill Main Drive
RAW_MILL_MAIN_DRIVE_CONFIG = EquipmentConfig(
    equipment_id="Raw_Mill_Main_Drive_RM1",
    name="Raw Mill Main Drive",
    motor=MotorSpecs(
        horsepower=5000.0,
        rated_voltage_v=4160.0,
        full_load_current_a=312.0,
        rated_speed_rpm=1788.0,
        rated_frequency_hz=60.0,
        frame="6310S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=35.0,
    current_warning_a=325.0,
    current_critical_a=350.0,
    temperature_warning_c=95.0,
    temperature_critical_c=115.0,
    alert_persistence_s=20,
    speed_feedback_source="encoder"
)

# Coal Mill - grinds coal for kiln burner
COAL_MILL_DRIVE_CONFIG = EquipmentConfig(
    equipment_id="Coal_Mill_Drive_CM1",
    name="Coal Mill Main Drive",
    motor=MotorSpecs(
        horsepower=250.0,
        rated_voltage_v=4160.0,
        full_load_current_a=50.0,
        rated_speed_rpm=1785.0,
        rated_frequency_hz=60.0,
        frame="4010S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=35.0,
    current_warning_a=53.0,
    current_critical_a=58.0,
    temperature_warning_c=90.0,
    temperature_critical_c=110.0,
    alert_persistence_s=20,
    speed_feedback_source="encoder"
)

# Cement Mill Main Drive - finish grinding
CEMENT_MILL_DRIVE_CONFIG = EquipmentConfig(
    equipment_id="Cement_Mill_Drive_FM1",
    name="Finish Mill Main Drive",
    motor=MotorSpecs(
        horsepower=5000.0,
        rated_voltage_v=4160.0,
        full_load_current_a=437.0,
        rated_speed_rpm=1780.0,
        rated_frequency_hz=60.0,
        frame="7010S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=35.0,
    current_warning_a=455.0,
    current_critical_a=480.0,
    temperature_warning_c=95.0,
    temperature_critical_c=115.0,
    alert_persistence_s=20,
    speed_feedback_source="encoder"
)

# Clinker Conveyor - moves clinker from cooler to storage
CLINKER_CONVEYOR_CONFIG = EquipmentConfig(
    equipment_id="Clinker_Conveyor_CC1",
    name="Clinker Pan Conveyor",
    motor=MotorSpecs(
        horsepower=75.0,
        rated_voltage_v=460.0,
        full_load_current_a=92.0,
        rated_speed_rpm=1775.0,
        rated_frequency_hz=60.0,
        frame="405T"
    ),
    max_frequency_hz=55.0,
    ambient_temperature_c=50.0,
    current_warning_a=97.0,
    current_critical_a=106.0,
    temperature_warning_c=95.0,
    temperature_critical_c=115.0,
    alert_persistence_s=30,
    speed_feedback_source="drive_estimated"
)

# Preheater Tower Fan - top cyclone stage
PREHEATER_FAN_CONFIG = EquipmentConfig(
    equipment_id="Preheater_Fan_PH1",
    name="Preheater Tower Fan",
    motor=MotorSpecs(
        horsepower=500.0,
        rated_voltage_v=4160.0,
        full_load_current_a=62.5,
        rated_speed_rpm=1785.0,
        rated_frequency_hz=60.0,
        frame="4510S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=50.0,
    current_warning_a=66.0,
    current_critical_a=72.0,
    temperature_warning_c=100.0,
    temperature_critical_c=120.0,
    alert_persistence_s=20,
    speed_feedback_source="drive_estimated"
)

# Limestone Crusher - primary impact crusher
LIMESTONE_CRUSHER_CONFIG = EquipmentConfig(
    equipment_id="Limestone_Crusher_LC1",
    name="Limestone Impact Crusher",
    motor=MotorSpecs(
        horsepower=600.0,
        rated_voltage_v=4160.0,
        full_load_current_a=75.0,
        rated_speed_rpm=1785.0,
        rated_frequency_hz=60.0,
        frame="4510S"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=30.0,
    current_warning_a=79.0,
    current_critical_a=86.0,
    temperature_warning_c=90.0,
    temperature_critical_c=110.0,
    alert_persistence_s=15,
    speed_feedback_source="encoder"
)

# Raw Meal Silo Aeration Fan - fluidizes raw meal in silo
SILO_AERATION_FAN_CONFIG = EquipmentConfig(
    equipment_id="Silo_Aeration_Fan_SA1",
    name="Raw Meal Silo Aeration Fan",
    motor=MotorSpecs(
        horsepower=25.0,
        rated_voltage_v=460.0,
        full_load_current_a=32.0,
        rated_speed_rpm=3540.0,
        rated_frequency_hz=60.0,
        frame="286T"
    ),
    max_frequency_hz=60.0,
    ambient_temperature_c=25.0,
    current_warning_a=34.0,
    current_critical_a=37.0,
    temperature_warning_c=85.0,
    temperature_critical_c=100.0,
    alert_persistence_s=45,  # low criticality, longer persistence
    speed_feedback_source="drive_estimated"
)

# Cement Screw Conveyor
CEMENT_SCREW_CONVEYOR_CONFIG = EquipmentConfig(
    equipment_id="Cement_Screw_Conv_SC1",
    name="Cement Screw Conveyor",
    motor=MotorSpecs(
        horsepower=40.0,
        rated_voltage_v=460.0,
        full_load_current_a=50.0,
        rated_speed_rpm=1775.0,
        rated_frequency_hz=60.0,
        frame="324T"
    ),
    max_frequency_hz=50.0,  # screw conveyors rarely run full speed
    ambient_temperature_c=28.0,
    current_warning_a=53.0,
    current_critical_a=58.0,
    temperature_warning_c=85.0,
    temperature_critical_c=100.0,
    alert_persistence_s=30,
    speed_feedback_source="drive_estimated"
)

EQUIPMENT_CATALOG = {
    equipment.equipment_id: equipment
    for equipment in (
        STACK_FAN_CONFIG,
        KILN_MAIN_DRIVE_CONFIG,
        KILN_ID_FAN_CONFIG,
        RAW_MILL_MAIN_DRIVE_CONFIG,
        COAL_MILL_DRIVE_CONFIG,
        CEMENT_MILL_DRIVE_CONFIG,
        CLINKER_CONVEYOR_CONFIG,
        PREHEATER_FAN_CONFIG,
        LIMESTONE_CRUSHER_CONFIG,
        SILO_AERATION_FAN_CONFIG,
        CEMENT_SCREW_CONVEYOR_CONFIG,
    )
}