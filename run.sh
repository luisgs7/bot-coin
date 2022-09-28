#!/bin/bash
echo "Let's Go!"

read  -p "Enter the database username: " database_user

sudo docker-compose down

sudo docker-compose up -d
echo "Wait 10 seconds, the database is initializing..."
sleep 10

sudo docker-compose exec db psql -U $database_user -d bot_data -f  /scripts/insert.sql

sudo docker-compose down

sudo docker-compose up -d
echo "Finished."