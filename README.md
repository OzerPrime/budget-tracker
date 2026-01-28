# budget-tracker
Income and Expense Tracking Application with Python and SQLite     

***🧾 Budget Tracker App***

A modern Income & Expense Tracking Application built with Python, SQLite, and CustomTkinter.

***✨ Features***

Add income records

Add expense records

Automatic date tracking

SQLite database for persistent storage

Calculate total income, total expenses, and net balance

Modern dark-themed GUI

Watermark branding

PNG logo support

***🛠️ Technologies Used***

Python 3

SQLite3

CustomTkinter

Pillow (PIL)


***🚀 How to Run***
# Requirements
- Python 3.8+ recommended
- pip

## How to run (recommended)

1. Clone the repo
```
git clone https://github.com/OzerPrime/budget-tracker.git
cd budget-tracker
```

2. Create and activate a virtual environment
- macOS / Linux:
```
python3 -m venv venv
source venv/bin/activate
```
- Windows (PowerShell):
```
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Initialize the database (if there is an init script)
- If there is a file named `init_db.py` or similar, run:
```
python init_db.py
```
- If there is a SQL schema (e.g. `schema.sql`), run:
```
sqlite3 budget.db < schema.sql
```
If there is no init step, the app may create the DB on first run — see app.py.

5. Run the application
```
python app.py
```
Or, if your system uses `python3`:
```
python3 app.py
```

6. Troubleshooting
- If you see `ModuleNotFoundError`, ensure requirements installed in the active venv.
- If you see `sqlite3.OperationalError: unable to open database file`, check that the application has write permission to the folder and that any configured DB path exists.
- If the README command (`python app.py`) doesn't match a file in repo, check the actual entrypoint:
```
ls -la
cat app.py
```
Then run the correct file name (e.g. `python main.py`).

If you still have issues, paste the full traceback from `python app.py` here.

Run the application:

python app.py




