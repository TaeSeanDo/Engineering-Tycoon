
"""
Sean Tierney
Product class
"""

class Product:
    """docstring for Robot"""
    def __init__(self, difficulty, consumer_utility, revenue):
        self.budget = 600 / difficulty
        self.consumer_utility = consumer_utility
        self.revenue = revenue
    def investment(self, consumer_utility_change, revenue_change, budget_change):
        self.consumer_utility += consumer_utility_change
        self.revenue += revenue_change
        self.budget += budget_change
