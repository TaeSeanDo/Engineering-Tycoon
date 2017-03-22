
"""
Sean Tierney
Product class
"""

class Product:
    """docstring for Robot"""
    def __init__(self, difficulty, revenue):
        self.budget = 600 / difficulty
        self.revenue = revenue
    def investment(self, revenue_change, budget_change):
        self.revenue += revenue_change
        self.budget += budget_change
