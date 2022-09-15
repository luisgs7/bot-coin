select * from table_coin order by id limit 5;


CREATE TABLE IF NOT EXISTS table_coin (
						id SERIAL PRIMARY KEY, 
                        name VARCHAR(15),
                        buy smallint, 
                        sell smallint, 
                        variation smallint);

                       
alter table table_coin add column if not exists date_time timestamptz; 


INSERT INTO table_coin VALUES (
							  8,
							  'name',
                               1.1, 
                               2.2, 
                               3.3,
                               default
                               );
                              
select date_time from table_coin; 



select timestamp with time zone '2018-04-02T09:00:00+09:30';
      

alter table table_coin 
alter column date_time set default current_timestamp;


UPDATE table_coin  set name='NAME', buy=1.1, sell=1.1, 
				   variation=1.1, date_time=default WHERE id=6;


SELECT * FROM "public"."table_coin" order by id LIMIT 5;     