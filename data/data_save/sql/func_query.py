'''Module that has functions that execute SQL queries.'''


def query_select_value(table_name: str) -> str:
    '''Function that performs a select on the corresponding table.'''
    query = f"SELECT id, name, buy, sell, variation \
            FROM {table_name};"
    return query


def query_insert_value(
    table_name: str, name: str, buy: float, sell: float, variation: float
) -> str:
    '''Function that executes an Inset on the corresponding table.'''
    query = f"INSERT INTO {table_name} \
                        VALUES (default, '{name}', {buy}, {sell}, {variation}, default);"
    return query


def query_update_value(
    table_name: str, _id: int, name: str, buy: float, sell: float, variation: float
) -> str:
    '''Function that performs an Update on the corresponding table.'''
    query = f"UPDATE {table_name} SET \
              name='{name}', \
              buy={buy}, \
              sell={sell}, \
              variation={variation}, \
              date_time=default \
              WHERE id={_id};"

    return query
