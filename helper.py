import os
from pathlib import Path


def get_data_root() -> str:
    return os.path.join(Path(__file__).parent, "input")


def get_data(day: int) -> str:
    filename = f"day{day:02d}.data"
    path = os.path.join(get_data_root(), filename)
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError
