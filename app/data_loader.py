import json
from pathlib import Path

def load_mock_data(filename="mock_data.json"):
    base_dir = Path(__file__).resolve().parent  # Directory where this script lives
    filepath = base_dir / filename

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Optional test run
if __name__ == "__main__":
    data = load_mock_data()
    print(data)
