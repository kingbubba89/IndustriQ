import csv
from dataclasses import asdict, fields
from pathlib import Path

from industriq.readings import EquipmentReading

def save_readingscsv(
        readings: list[EquipmentReading],
        file_path: Path,
) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)

    column_names = [field.name for field in fields(EquipmentReading)]

    with file_path.open("w", newline="", encoding = "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames = column_names)
        writer.writeheader()

        for reading in readings:
            row = asdict(reading)
            row["timestamp"] = reading.timestamp.isoformat()
            writer.writerow(row)