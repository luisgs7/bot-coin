from utils import constants, connect
from query_response.func_query import query


class DataConnect:
    """Class responsible for performing operations on the database."""

    def __init__(self, _id):
        self._con = connect.link()
        self.cur = self._con.cursor()
        self._tb_name = constants.TABLE_NAME
        self._id = _id
        print("Database running...")

    def select_coin_id(self):
        """Perform select on the database."""
        res = self.cur.execute(query.query_select_value(self._tb_name, self._id))
        res = self.cur.fetchone()
        return res