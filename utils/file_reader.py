import json
from pathlib import Path

base_path = Path.cwd().joinpath('..', 'tests', 'data')
print(base_path)


def read_file(file_name):
    """
    Reads a file and returns the contents as a string.
    """
    path = get_file_with_json_extension(file_name)
    with path.open(mode='r') as file:
        return json.load(file)


def get_file_with_json_extension(file_name):
    if '.json' in file_name:
        path = base_path.joinpath(file_name)
    else:
        path = base_path.joinpath(f'{file_name}.json')
    return path
