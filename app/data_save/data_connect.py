import psycopg2
from sql import func_query
from decouple import config

_BASE_URL: str = config("DATABASE_URL")


class DataConnect():

    def __init__(self):
        self._con = psycopg2.connect(_BASE_URL)
        self.cur = self._con.cursor()
        self._tb_name = "table_coin"
        print("Database runing...")

    def select_coin(self):
        res = self.cur.execute(func_query.query_select_value(self._tb_name))
        res = self.cur.fetchone()
        return res
    
    def _insert_coin(self, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_insert_value(self._tb_name, name, buy, sell, variation))
        self._con.commit()
        return None
    
    def update_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_update_value(self._tb_name, id, name, buy, sell, variation))
        self._con.commit()
        return None

    def _create_table(self):
        res = self.cur.execute(func_query.query_create_table(self._tb_name))
        return f"Criada a {self._tb_name}"


pessoa = "Pedro"
pessoa2 = "José"
#print(f"Create Table: {DataConnect().create_table()}")
#print(f"Insert values: {DataConnect().insert_coin(name=pessoa, buy=1.34, sell=1.56, variation=-1.34)}")

#print(a[0])
#print(f"Update Values: {DataConnect().update_coin(id=3,name=pessoa2, buy=2.4, sell=3.8, variation=1.43)}")

a = DataConnect().select_coin()
print(f"SELECT Values: {a}")

