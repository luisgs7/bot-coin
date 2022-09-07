import psycopg2
from decouple import config

BASE_URL: str = config("DATABASE_URL")

from sql import func_query

con = psycopg2.connect(BASE_URL)


print("Database Conectado")

cur = con.cursor()

tb_name = "table_coin"
print("Conectado...")
'''
cur.execute(func_query.query_create_table(tb_name))
print(f"Criada a tabela: {tb_name}")
'''
sql = 'create table if not exists cidade (id serial primary key, nome varchar(100), uf varchar(2))'
cur.execute(sql)

sql = "insert into cidade values (default,'São Paulo','sp')"

cur.execute(sql)
con.commit()
cur.execute('select * from cidade')
recset = cur.fetchall()
for rec in recset:
    print(rec)

con.close()