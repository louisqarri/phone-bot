# 📱 PhoneBot: a small data pipeline project

A small end-to-end data pipeline in Python: data goes from a **JSON file** into a **SQLite database**, and from the database to a **web page**. The phone data is only a simple sample dataset to carry through the pipeline.

> Personal learning project. The sample data is limited and **not up to date**. It's not connected to any phone brand or store.

## Data flow

```
data/smartphones.json  →  load_data.py  →  SQLite database  →  Brain  →  Flask web page
      (source)             (load)            (storage)         (read)       (presentation)
```

1. **Source:** `data/smartphones.json` holds the sample phones.
2. **Load:** `load_data.py` reads the JSON and inserts each phone into SQLite with SQLAlchemy. It skips phones that are already in the database, so it is **safe to run more than once**.
3. **Storage:** the `Phone` table is defined once in `database.py` and shared by the other files.
4. **Read:** the `Brain` class loads the phones from the database and can find a phone, show its specs, or compare two phones.
5. **Present:** `app.py` connects the `Brain` to the Flask pages (home, specs, compare, readme). A terminal version of the same logic is in `main.py`.

## What it does

- Shows the specs of one phone
- Compares two phones
- Picks the phones from dropdown lists, so there are no typing mistakes

## Built with

- Python
- SQLAlchemy and SQLite
- Flask and Jinja templates
- HTML and CSS (no JavaScript)

## How to run it

```bash
# 1. Get the project
git clone https://github.com/louisqarri/phone-bot.git
cd phone-bot

# 2. Create a virtual environment and install the requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Create the database and load the data from the JSON file
python3 load_data.py

# 4. Start the web app
python3 app.py
```

Open http://127.0.0.1:5000 in your browser. For the terminal version: `python3 main.py`.

Run the commands from the project folder, because the database path is relative.

## Project structure

```
phone-bot/
├── app.py               # Flask app: pages and routes
├── brain.py             # Brain class: reads the database, builds the answers
├── database.py          # Phone table (SQLAlchemy) and the database connection
├── load_data.py         # JSON -> SQLite loader (safe to re-run)
├── main.py              # Terminal version
├── data/
│   └── smartphones.json # Source data
├── templates/           # HTML pages
├── static/css/          # Stylesheet
├── requirements.txt
└── README.md
```

## Design choices

- **Definitions and actions are separated.** `database.py` only defines the table and the connection, so importing it never changes anything. Loading data is a separate script you run on purpose.
- **The logic lives in one class.** The terminal version and the web version use the same `Brain`.
- **The app reads only from the database**, never from the JSON file.

## Limitations

- Small sample dataset, not kept up to date
- No tests yet
- Some phones have no ultra wide or telephoto camera, and those fields show as empty values

## About

Built by Louis as a personal Python learning project, to practise the extract, load and present steps of a data pipeline.
