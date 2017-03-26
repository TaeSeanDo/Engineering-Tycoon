#Sets up the class for mobile devices
from ProductClass import Product
class mobile_devices(Product):
    def __init__(self, difficulty, colors, headjack_YN, battery_life, material,
        processor_proficiency = 1, internal_storage_capacity = 1, revenue = 0):
        self.colors = colors
        self.headjack_YN = headjack_YN
        self.battery_life = battery_life
        self.material = material

#Investment function keeps track of money
    def investment(self, revenue_change, budget_change):
        self.revenue += revenue_change
        self.budget += budget_change
