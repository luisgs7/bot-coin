""" Create Table """
CREATE TABLE IF NOT EXISTS table_coin (
						id SERIAL PRIMARY KEY, 
                        name VARCHAR(15),
                        buy smallint, 
                        sell smallint, 
                        variation smallint);
                    

"""Insert Value"""
INSERT INTO table_coin VALUES (id, 
                               'name',
                               buy, 
                               sell, 
                               variation);

"""DROP TABLE"""
DROP TABLE table_coin;




