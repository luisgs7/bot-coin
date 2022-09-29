### Bot Coin
This project consists, in a simplified form, of a bot for Telegram, with the purpose of studies, without any commercial connection, which allows access to quotes of the following currencies in relation to the real:
- USD DÓLAR
- EUR EURO
- CAD CANADENSE
- JPY IENE
- MERCADO BITCOIN

#### The Bot is available for access through the link:

### Stack:

<img src="https://raw.githubusercontent.com/luisgs7/images-projects/main/bot-coin/bot-coin.png">

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

Both applications were developed using the Python programming language, and sql to communicate with the database. The API used by the data app is from: <a href="https://hgbrasil.com/status/finance">HGBrasil Finance</a>, which uses the platform's free plan.

### Project installation

To start, create a bot on telegram, following the instructions on the official website, and save the generated token: <a href="https://core.telegram.org/bots">Telegram Bot API</a>. 

Then access the website: <a href="https://hgbrasil.com/">HGBrasil</a>, create a free account and generate an access key, which will be added to an .env file in the project.

Also, the project has 3 .env.example files, use them as a base to create 3 .env files, in the same location, each file contains environment variables that should not be added to version control in any way. In this file you will add information such as telegram bot token, API key, database connection, among other important information. It is extremely necessary to fill it in the right way, so that the application works correctly.

The only software that needs to be installed in the development environment are docker and docker-compose.

To start the project for the first time, use a shell script in the root of the project. However, first give execute permissions to the script file using the command below.
```
sudo chmod 775 run.sh
```

Now just run this shell script with the command below. Once the script runs, you will be asked to enter the password for the database user you added to the .env file, then just wait a few seconds for the project to be ready to use.
```
./run.sh
```
From the second time the project is started, you can use this command to start the project again.
```
docker-compose up -d
```

### Bot Initialized

<p><img alt="Image" title="icon" src="https://raw.githubusercontent.com/luisgs7/images-projects/main/bot-coin/telegram-bot-coin.jpg" width="200" height="400"></p>

If you have any doubts, please add a problem to the repository, which will be answered as soon as possible.

### Next steps of the project.

- Add unit tests to the project.
- Add new functionality to convert user-supplied values.

### How to contribute to the project.

If you want to contribute to the project, just fork and send a pullrequest with the new functionality or bug fixes. Remembering that it is necessary that the github actions approve all the actions of the project, so that the contribution is analyzed.
