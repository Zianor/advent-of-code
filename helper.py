import os
from pathlib import Path


def get_data_root() -> Path:
    return os.path.join(Path(__file__).parent, 'input')


def get_data(day) -> Path:
    if day < 10:
        filename = 'day0' + str(day) + '.data'
    else:
        filename = 'day' + str(day) + '.data'
    path = os.path.join(get_data_root(), filename)
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError
    return None
