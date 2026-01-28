import sqlite3
from datetime import datetime
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

connection = sqlite3.connect("budget.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    amount INTEGER,
    date TEXT
)
""")

connection.commit()
connection.close()

def add_income():
    amount = income_entry.get()
    if amount.isdigit():
        date = datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect("budget.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO transactions (type, amount, date) VALUES (?, ?, ?)",
            ("income", int(amount), date)
        )
        conn.commit()
        conn.close()
        income_entry.delete(0, "end")

def add_expense():
    amount = expense_entry.get()
    if amount.isdigit():
        date = datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect("budget.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO transactions (type, amount, date) VALUES (?, ?, ?)",
            ("expense", int(amount), date)
        )
        conn.commit()
        conn.close()
        expense_entry.delete(0, "end")

def show_balance():
    conn = sqlite3.connect("budget.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cur.fetchone()[0]
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cur.fetchone()[0]
    conn.close()

    if total_income is None:
        total_income = 0
    if total_expense is None:
        total_expense = 0

    balance_label.configure(
        text=f"Income: {total_income} TL\nExpense: {total_expense} TL\nBalance: {total_income - total_expense} TL"
    )

app = ctk.CTk()
app.geometry("500x600")
app.title("Budget Tracker")

title_label = ctk.CTkLabel(app, text="Budget Tracker", font=("Arial", 28))
title_label.pack(pady=20)

income_entry = ctk.CTkEntry(app, placeholder_text="Income amount")
income_entry.pack(pady=10)

income_button = ctk.CTkButton(app, text="Add Income", command=add_income)
income_button.pack(pady=5)

expense_entry = ctk.CTkEntry(app, placeholder_text="Expense amount")
expense_entry.pack(pady=10)

expense_button = ctk.CTkButton(app, text="Add Expense", command=add_expense)
expense_button.pack(pady=5)

balance_button = ctk.CTkButton(app, text="Show Balance", command=show_balance)
balance_button.pack(pady=20)

balance_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
balance_label.pack(pady=10)

watermark = ctk.CTkLabel(
    app,
    text="ozer\nprime",
    font=("Arial", 14),
    text_color="#444444"
)
watermark.place(relx=0.5, rely=0.95, anchor="center")

try:
    logo_image = ctk.CTkImage(
        light_image=Image.open("logo.png"),
        dark_image=Image.open("logo.png"),
        size=(120, 120)
    )
    logo_label = ctk.CTkLabel(app, image=logo_image, text="")
    logo_label.pack(pady=10)
except:
    pass

app.mainloop()
