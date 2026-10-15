from data.data_io import save_readingscsv
from industriq.equipment_catalog import KILN_ID_FAN_CONFIG, EQUIPMENT_CATALOG, STACK_FAN_CONFIG
from industriq.report import print_reading
from industriq.simulator import simulate_fan
from pathlib import Path

def main():
   readings = simulate_fan(STACK_FAN_CONFIG)
   project_root = Path(__file__).resolve().parents[2]
   output_path = project_root / "data" / "stack_fan_readings.csv"

   save_readingscsv(readings, output_path)

   print(f"IndustriQ | {STACK_FAN_CONFIG.name}")
   print(f"Generated {len(readings)} simulated readings")

   print_reading("First reading", readings[0])
   print_reading("Last reading", readings[-1])

if __name__ == "__main__":
    main()