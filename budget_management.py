# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters.
# Problem Statement: You are required to build a Personal Budget Management application. The application will 
# manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private 
# and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name 
# and allocated budget. - Initialize these attributes in the constructor.
# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget


# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the 
# allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).
# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation 
# checks in place.

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            raise ValueError("Category name must be a non-empty string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  
        else:
            raise ValueError("Allocated budget must be a positive number.")
    

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. 
# Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            raise ValueError("Invalid expense amount. It should be a positive number and less than or equal to the remaining budget.")


# Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, 
# allocated budget, and remaining budget after expenses.
# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
