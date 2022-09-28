""" CREATE DATABASE """
CREATE DATABASE db_app;


""" CREATE TABLE """
CREATE TABLE IF NOT EXISTS bot_coin_table (
						id SERIAL PRIMARY KEY, 
                        name VARCHAR(15),
                        buy real, 
                        sell real, 
                        variation real,
                        date_time timestamp  default current_timestamp);


""" MODIFY THE TIME ZONE TO YOUR LOCATION. """
ALTER DATABASE bot_coin_table SET timezone TO 'America/Araguaina';                    


"""INSERT VALUES"""
INSERT INTO bot_coin_table(id, name, buy, sell, variation, date_time) 
			   VALUES (default, 'name1', 0.0, 0.0, 0.0, default);

INSERT INTO bot_coin_table(id, name, buy, sell, variation, date_time) 
			   VALUES (default, 'name2', 0.0, 0.0, 0.0, default);

INSERT INTO bot_coin_table(id, name, buy, sell, variation, date_time) 
			   VALUES (default, 'name3', 0.0, 0.0, 0.0, default);

INSERT INTO bot_coin_table(id, name, buy, sell, variation, date_time) 
			   VALUES (default, 'name4', 0.0, 0.0, 0.0, default);

INSERT INTO bot_coin_table(id, name, buy, sell, variation, date_time) 
			   VALUES (default, 'name5', 0.0, 0.0, 0.0, default);


"""SELECT VALUES TABLE"""
SELECT * FROM bot_coin_table;

""" OK """




