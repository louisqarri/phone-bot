# 📱 PhoneBot

A small web app to look up the specifications of a smartphone, or to compare two phones side by side.

Pick the phone(s) from a dropdown, press the button, and the result appears on the page.

> Personal learning project. The data is **not up to date** and not connected to any phone brand or store.

## Features

- **Show specs** of a single phone
- **Compare** two phones
- Phone data stored in a **SQLite database**
- Simple, minimal web interface (HTML and CSS, no JavaScript)
- A terminal version of the same bot (`main.py`)

## Built with

- Python
- Flask
- SQLAlchemy and SQLite
- HTML and CSS (Jinja templates)

## How to run it

```bash
# 1. Get the project
git clone https://github.com/louisqarri/phone-bot.git
cd phone-bot

# 2. Create a virtual environment and install the requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Create the database and load the phones from the JSON file
python3 load_data.py

# 4. Start the web app
python3 app.py
```

Then open http://127.0.0.1:5000 in your browser.

To use the terminal version instead: `python3 main.py`

## Project structure

```
phone-bot/
├── app.py               # Flask app: the pages (home, compare, specs, readme)
├── brain.py             # Brain class: finds phones and builds the answers
├── database.py          # The Phone table (SQLAlchemy) and the database connection
├── load_data.py         # One-time script: JSON -> SQLite database
├── main.py              # Terminal version of the bot
├── data/
│   └── smartphones.json # The phone data
├── templates/           # HTML pages
├── static/css/          # Stylesheet
├── requirements.txt
└── README.md
```

## How it works

1. `load_data.py` reads `data/smartphones.json` and stores every phone in the SQLite database (it skips phones that are already there).
2. `Brain` loads the phones from the database and can find a phone by model name, show its specs, or compare two phones.
3. `app.py` connects `Brain` to the web pages: the form sends the chosen model(s), and the result is shown on the same page.

## About the data

The phone list is limited and **not kept up to date**. Prices, models and specs may be outdated. Use it for fun, not for buying decisions.

## About

Built by Louis as a personal Python learning project.
