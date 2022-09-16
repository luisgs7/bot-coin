"""Module responsible for performing operations on the database."""
from utils import constants, connect
from data_save.sql import func_query


class DataConnect:
    """Class responsible for performing operations on the database."""

    def __init__(self):
        self._con = connect.link()
        self.cur = self._con.cursor()
        self._tb_name = constants.TABLE_NAME
        print("Database running...")

    def select_coin(self):
        """Perform select on the database."""
        res = self.cur.execute(func_query.query_select_value(self._tb_name))
        res = self.cur.fetchone()
        return res

    def _insert_coin(self, name: str, buy: float, sell: float, variation: float):
        """Insert coins into the database."""
        self.cur.execute(
            func_query.query_insert_value(self._tb_name, name, buy, sell, variation)
        )
        self._con.commit()

    def update_coin(
        self, _id: int, name: str, buy: float, sell: float, variation: float
    ):
        """Coin update in the database."""
        self.cur.execute(
            func_query.query_update_value(
                self._tb_name, _id, name, buy, sell, variation
            )
        )
        self._con.commit()
        print("Update data...")

    def _create_table(self):
        """Method to create the database, used only the first time the project is started."""
        self.cur.execute(func_query.query_create_table(self._tb_name))
