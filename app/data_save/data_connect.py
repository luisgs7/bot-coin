import sqlite3
import os


class DataConnect():

    def __init__(self):
        self.table_name = "table_coin"
        self.__dir_db = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.con = sqlite3.connect(f"{self.__dir_db}/app.db")
        self.cur = self.con.cursor()
    
    def select_curencies(self):
        res = self.cur.execute(
            f"SELECT id, name, buy, sell, variation \
            FROM {self.table_name} \
            WHERE id and 1" \
        )
        res = res.fetchall()
        return res
    
    def insert_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(
            f"INSERT INTO {self.table_name} VALUES({id}, '{name}', {buy}, {sell}, {variation})"
        )
        self.con.commit()
        return None
    
    def update_coin(self, id: int, name: str, buy: float, sell: float, variation: float):
        self.cur.execute(
            f"UPDATE {self.table_name} SET \
              name='{name}', \
              buy={buy}, \
              sell={sell}, \
              variation={variation} \
              WHERE id=1" \
        )
        self.con.commit()
        return None

    def create_table(self):
        res = self.cur.execute("CREATE TABLE IF NOT EXISTS table_coin( \
                                id INT NOT NULL, \
                                name varchar, \
                                buy NUMERIC, \
                                sell NUMERIC, \
                                variation NUMERIC)")
        
        return None
    
    def drop_table(self):
        self.cur.execute("DROP TABLE table_coin")
        return "OK"
pessoa = "Pedro"
pessoa2 = "José"
#print(f"Create Table: {DataConnect().create_table()}")
#print(f"Insert values: {DataConnect().insert_coin(id=1, name=pessoa, buy=1.34, sell=1.56, variation=-1.34)}")
print(f"SELECT Values: {DataConnect().select_curencies()}")
#print(f"Update Values: {DataConnect().update_coin(id=1, name=pessoa2, buy=2.4, sell=3.8, variation=1.43)}")

#print(f'Drop Table: {DataConnect().drop_table()}')