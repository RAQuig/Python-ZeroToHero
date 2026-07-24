"""
MODULE 2 PROJECT: CLI Expense & Budget Tracker
Instructions: Run this script to track expenses. Data persists in 'expenses.json'.
Modify this file with your group to add new features like budget caps or spending graphs!
"""

import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    """Loads expenses from JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Warning: Could not read expense file. Starting fresh.")
        return []

def save_expenses(expenses):
    """Saves the expenses list to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    category = input("Enter category (e.g., Food, Games, Transport): ").strip().capitalize()
    
    try:
        amount = float(input("Enter amount ($): "))
    except ValueError:
        print("❌ Invalid amount! Expense not added.")
        return

    description = input("Enter description: ").strip()

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. [{item['category']}] ${item['amount']:.2f} - {item['description']}")
        total += item["amount"]

    print("-" * 30)
    print(f"Total Spent: ${total:.2f}")

def view_summary_by_category(expenses):
    print("\n--- Category Breakdown ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for item in expenses:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n" + "=" * 35)
        print("      EXPENSE & BUDGET TRACKER      ")
        print("=" * 35)
        print("1. View All Expenses")
        print("2. Add New Expense")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            view_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            view_summary_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
