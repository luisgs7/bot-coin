#!/bin/bash
echo "Let's Go!"

read  -p "Digite o nome do usuário do banco de dados: " database_user

sudo docker-compose down

sudo docker-compose up -d
echo "Wait 10 seconds, the database is initializing..."
sleep 10

sudo docker-compose exec db psql -U $database_user -d bot_data -f  /scripts/insert.sql

sudo docker compose down

sudo docker-compose up
echo "Finished."