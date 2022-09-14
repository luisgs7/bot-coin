"""File responsible for formatting the data."""
from typing import List


def data_format(data: List) -> List:
    """Function responsible for formatting data correctly."""
    count = 0
    for item in data:
        if item == None:  # noqa pylint: disable= singleton-comparison
            data[count] = 0
        count += 1
    return data
