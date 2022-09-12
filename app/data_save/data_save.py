"""Module responsible for saving data in the database."""
from typing import Dict
from data_save.data_connect import DataConnect


def data_save(data: Dict, id_key: int):
    """Function to save data."""
    DataConnect().update_coin(
        _id=id_key, name=data[0], buy=data[1], sell=data[2], variation=data[3]
    )
