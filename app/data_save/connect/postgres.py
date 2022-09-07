import psycopg2
from app.data_save.connect.sql import func_query


class DataConnect():

    def __init__(self):
        self.con = psycopg2.connect("postgres://nxmhpaof:buSco67i267kihD7ouvLjE7grssbOKJk@kesavan.db.elephantsql.com/nxmhpaof")
        self.cur = self.con.cursor()
        self._tb_name = "table_coin"

    def select_curencies(self):
        res = self.cur.execute(func_query.query_select_value(self._tb_name))
        res = res.fetchall()
        return res
    
    def insert_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_insert_value(self._tb_name, id, name, buy, sell, variation))
        self.con.commit()
        return None
    
    def update_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(func_query.query_update_value(self._tb_name, id, name, buy, sell, variation))
        self.con.commit()
        return None

    def create_table(self):
        res = self.cur.execute(func_query.query_create_table(self._tb_name))
        return None
    
    def drop_table(self):
        self.cur.execute(func_query.query_drop_db(self._tb_name))
        return "DROP"



pessoa = "Pedro"
pessoa2 = "José"
print(f"Create Table: {DataConnect().create_table()}")
#print(f"Insert values: {DataConnect().insert_coin(id=1, name=pessoa, buy=1.34, sell=1.56, variation=-1.34)}")
#a = DataConnect().select_curencies()
#print(f"SELECT Values: {a}")
#print(a[0])
#print(f"Update Values: {DataConnect().update_coin(id=1, name=pessoa2, buy=2.4, sell=3.8, variation=1.43)}")

#print(f'Drop Table: {DataConnect().drop_table()}')
#print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))