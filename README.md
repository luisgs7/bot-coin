### Bot Coin
This project consists, in a simplified form, of a bot for Telegram, with the purpose of studies, without any commercial connection, which allows access to quotes of the following currencies in relation to the real:
- USD DÓLAR / BRL REAL
- EUR EURO / BRL REAL
- CAD CANADENSE / BRL REAL
- JPY IENE / BRL REAL
- MERCADO BITCOIN / BRL REAL
### Stack:
This project uses as few Python libraries as possible, communication with the database is performed via sql, and it uses flake8 and pylint to guarantee an algorithm within the PEP8 standard, in addition to the following technologies:
- Python: 3.10.6
- Docker and Docker Compose
- PostgreSQL
- Github Actions for Continuous Integrations
- Telegram Rest API

In addition, the following Python libraries are used:
```
requests==2.28.1
python-decouple==3.6
psycopg2==2.9.3
flake8==5.0.4
pytest==7.1.3
pylint==2.15.2
pylint==2.15.2
```
### Project explanation

This project consists of two independent applications, the first application, data, communicates with a financial data API and updates the data provided by the api in a postgresql database every 5 minutes, this query is performed through a schedule .

The other application, the bot, consists of an app that communicates with the Telegram API and with the same database as the data application, in this way the bot communicates and only knows of the existence of a single point of truth, the database of data. At no time does it communicate with the financial API.

Both applications were developed using the Python programming language, and sql to communicate with the database. The API used by the data app is from: https://hgbrasil.com/status/finance, which uses the platform's free plan.

### Project installation

To start, create a bot on telegram, following the instructions on the official website, and save the generated token: https://core.telegram.org/bots

With the exception of the database, the other applications use docker and docker compose to run the application, just having these tools installed on your machine. For the database you can use, for example, an online tool, such as: https://www.elephantsql.com/, which makes it possible to create a postgreslq database for free.

After creating the database, it is necessary to create a table and add some values to be updated by the data application, for this just execute the sql queries from this file: **sql file**

Then access the website: https://hgbrasil.com/, create a free account and generate an access key, which will be added to an .env file in the project.

Also, use the 2 .env.example files, inside each project as a base to create a file in each project, with the name .env, this file contains environment variables that should not be added to version control in any way . In this file you will add information such as telegram bot token, API key, database connection, among other important information. It is extremely necessary to fill it in the correct way, so that the application can work correctly.

Okay, now you can create the docker containers, using the following command:
```
docker-compose build
```

And then to run the project, just use this command:
```
docker-compose up 
```
### Bot Initialized

<p><img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/images-projects/main/bot-coin/telegram-bot-coin.jpg" width="200" height="400"></p>

If you have any doubts, please add a problem to the repository, which will be answered as soon as possible.

### Project installation

With the exception of the database, the other applications use docker and docker compose to run the application, just having these tools installed on your machine. For the database you can use, for example, an online tool, such as: https://www.elephantsql.com/, which makes it possible to create a postgreslq database for free.

After creating the database, it is necessary to create a table and add some values ​​to be updated by the data application, for this just execute the sql queries from this file: sql file
Then access the website: https://hgbrasil.com/, create a free account and generate an access key, which will be added to an .env file in the project.
In addition, the .env files of both projects must be filled in with correct values, as a base you must use the .env.example file, with the corresponding information, according to the instructions of each example file.
Okay, now you can create the docker containers, using the following command:
And then to run the project, just use this command:
If you have any doubts, please add a problem to the repository, which will be answered as soon as possible.

### Next steps of the project.

- Add unit tests to the project.
- Add new functionality to convert user-supplied values.

### How to contribute to the project.

If you want to contribute to the project, just fork and send a pullrequest with the new functionality or bug fixes. Remembering that it is necessary that the github actions approve all the actions of the project, so that the contribution is analyzed.
