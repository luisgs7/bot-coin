def query_create_table(table_name: str) -> str:
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ( \
            id SERIAL PRIMARY KEY, \
            name VARCHAR(15), \
            buy smallint, \
            sell smallint, \
            variation smallint);"
            
    return query

def query_select_value(table_name: str) -> str:
    query = f"SELECT id, name, buy, sell, variation \
            FROM {table_name};" 
    return query


def query_insert_value(table_name: str,
                       name: str, buy: float,
                       sell: float, variation: float) -> str:
    query = f"INSERT INTO {table_name} \
                        VALUES (default, '{name}', {buy}, {sell}, {variation});"
    return query

def query_update_value(table_name: str, id: int,
                       name: str, buy: float,
                       sell: float, variation: float) -> str:
    query = f"UPDATE {table_name} SET \
              name='{name}', \
              buy={buy}, \
              sell={sell}, \
              variation={variation} \
              WHERE id={id};"
    
    return query

def query_drop_db(table_name: str) -> str:
    query = f"DROP TABLE {table_name};"
    return query