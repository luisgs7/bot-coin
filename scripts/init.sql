\c bot_data


CREATE TABLE bot_coin_table (
						id SERIAL NOT NULL PRIMARY KEY, 
                        name VARCHAR(30)NOT NULL,
                        buy REAL NOT NULL, 
                        sell REAL NOT NULL, 
                        variation REAL NOT NULL,
                        date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

