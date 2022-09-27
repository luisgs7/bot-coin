""" CREATE DATABASE """
CREATE DATABASE db_app;


""" CREATE TABLE """
CREATE TABLE IF NOT EXISTS table_app (
						id SERIAL PRIMARY KEY, 
                        name VARCHAR(15),
                        buy real, 
                        sell real, 
                        variation real,
                        date_time timestamp  default current_timestamp);


""" MODIFY THE TIME ZONE TO YOUR LOCATION. """
ALTER DATABASE table_app SET timezone TO 'America/Araguaina';                    


"""INSERT VALUES"""
INSERT INTO table_app(id, name, buy, sell, variation, date_time) 
			   VALUES (1, 'name', 2.12, 2.23, 3.31, default);

INSERT INTO table_app(id, name, buy, sell, variation, date_time) 
			   VALUES (2, 'name', 3.12, 3.23, 3.31, default);

INSERT INTO table_app(id, name, buy, sell, variation, date_time) 
			   VALUES (3, 'name', 4.12, 4.23, 3.31, default);

INSERT INTO table_app(id, name, buy, sell, variation, date_time) 
			   VALUES (4, 'name', 5.12, 5.23, 3.31, default);

INSERT INTO table_app(id, name, buy, sell, variation, date_time) 
			   VALUES (5, 'name', 6.12, 6.23, 3.31, default);


"""SELECT VALUES TABLE"""
SELECT * FROM table_app;

""" OK """




