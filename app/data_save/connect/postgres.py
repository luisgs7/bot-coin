import psycopg2
from sql import func_query
from decouple import config

BASE_URL: str = config("DATABASE_URL")


class DataConnect():

    def __init__(self):
        self.con = psycopg2.connect(BASE_URL)
        self.cur = self.con.cursor()
        self._tb_name = "table_coin"
        print("Conectado...")

    def select_curencies(self):
        res = self.cur.execute(func_query.query_select_value(self._tb_name))
        res = self.cur.fetchall()
        return res
    
    def insert_coin(self, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_insert_value(self._tb_name, name, buy, sell, variation))
        self.con.commit()
        return None
    
    def update_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_update_value(self._tb_name, id, name, buy, sell, variation))
        self.con.commit()
        return None

    def create_table(self):
        res = self.cur.execute(func_query.query_create_table(self._tb_name))
        return f"Criada a {self._tb_name}"
    
    def drop_table(self):
        self.cur.execute(func_query.query_drop_db(self._tb_name))
        return "DROP"



pessoa = "Pedro"
pessoa2 = "José"
#print(f"Create Table: {DataConnect().create_table()}")
#print(f"Insert values: {DataConnect().insert_coin(name=pessoa, buy=1.34, sell=1.56, variation=-1.34)}")

#print(a[0])
#print(f"Update Values: {DataConnect().update_coin(id=3,name=pessoa2, buy=2.4, sell=3.8, variation=1.43)}")

a = DataConnect().select_curencies()
print(f"SELECT Values: {a}")

print(f'Drop Table: {DataConnect().drop_table()}')
