'''Module that has functions that execute SQL queries.'''


def query_select_value(table_name: str, _id) -> str:
    '''Function that performs a select on the corresponding table.'''
    print("Bot querying the data...")
    query = f"SELECT name, buy, variation, date_time \
            FROM {table_name} where id = {_id};"
    return query
