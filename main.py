import csv
import os

FILENAME = 'expenses.csv'

# Initialize CSV if not present
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Amount', 'Category', 'Description'])

def add_expense(amount, category, description):
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
    print("Expense added successfully!")

def view_expenses():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"Amount: {row[0]} | Category: {row[1]} | Description: {row[2]}")

def total_by_category():
    totals = {}
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[0])
            totals[category] = totals.get(category, 0) + amount
    print("\n--- Total Expenses by Category ---")
    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

def main():
    initialize_file()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()
