# plugins/inputs.py
import csv
import json
from typing import List, Any
from core.contracts import PipelineService


class CSVReader:
    """Reads CSV files and sends data to the Core engine via PipelineService."""

    def __init__(self, service: PipelineService):
        # Optional runtime check
        from typing import cast
        assert hasattr(service, "execute"), "Injected service must implement execute()"
        self.service = cast(PipelineService, service)

    def read(self, file_path: str) -> None:
        """Read a CSV file and send data to the Core."""
        try:
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data: List[Any] = list(reader)
            self.service.execute(data)
        except FileNotFoundError:
            print(f"ERROR: CSV file '{file_path}' not found.")
        except Exception as e:
            print(f"ERROR: Failed to read CSV file '{file_path}': {e}")


class JSONReader:
    """Reads JSON files and sends data to the Core engine via PipelineService."""

    def __init__(self, service: PipelineService):
        # Optional runtime check
        from typing import cast
        assert hasattr(service, "execute"), "Injected service must implement execute()"
        self.service = cast(PipelineService, service)

    def read(self, file_path: str) -> None:
        """Read a JSON file and send data to the Core."""
        try:
            with open(file_path, encoding="utf-8") as f:
                data: List[Any] = json.load(f)
            self.service.execute(data)
        except FileNotFoundError:
            print(f"ERROR: JSON file '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"ERROR: JSON file '{file_path}' is malformed.")
        except Exception as e:
            print(f"ERROR: Failed to read JSON file '{file_path}': {e}")