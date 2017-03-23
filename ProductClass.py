
"""
Sean Tierney
Product class
"""

class Product:
    """docstring for Robot"""
    def __init__(self, difficulty, revenue):
        self.budget = 600 / difficulty
        self.revenue = revenue
    def investment(self, revenue_increase, budget_decrease):
        self.revenue += revenue_increase
        self.budget -= budget_decrease
