
"""
Sean Tierney
Product class
"""

class Product:
    """docstring for Robot"""
    def __init__(self, difficulty, revenue):
        self.budget = 30000 / difficulty
        self.revenue = revenue
    def investment(self, revenue, budget_decrease):
        self.revenue += revenue
        self.budget -= budget_decrease
