class ExpenseTracker:
  def __init__(self):
      self.expenses = []

  def add_expense(self, amount, category, description):
      expense = {
          'amount': amount,
          'category': category,
          'description': description
      }
      self.expenses.append(expense)
      print(f"Expense added: ${amount} for {category} - {description}")

  def view_expenses(self):
      if not self.expenses:
          print("No expenses recorded yet.")
      else:
          print("Your expenses:")
          for expense in self.expenses:
              print(f"${expense['amount']} - {expense['category']} - {expense['description']}")

  def total_expenses(self):
      total = sum(expense['amount'] for expense in self.expenses)
      print(f"Total expenses: ${total}")

def main():
  tracker = ExpenseTracker()

  while True:
      print("\nExpense Tracker Menu:")
      print("1. Add Expense")
      print("2. View Expenses")
      print("3. View Total Expenses")
      print("4. Exit")

      choice = input("Choose an option: ")

      if choice == '1':
          amount = float(input("Enter the amount spent: "))
          category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
          description = input("Enter a brief description: ")
          tracker.add_expense(amount, category, description)
      elif choice == '2':
          tracker.view_expenses()
      elif choice == '3':
          tracker.total_expenses()
      elif choice == '4':
          print("Exiting Expense Tracker. Goodbye!")
          break
      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()