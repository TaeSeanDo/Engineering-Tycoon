#Sets up the class for mobile devices
class mobile_devices:
    def __init__(self, difficulty, colors, processor_proficiency = 1, internal_storage_capacity = 1, \
headjack_YN, battery_life, material, revenue = 0,  price = 0):
        self.budget = 600000/difficulty
        self.colors = colors
        self.headjack_YN = headjack_YN
        self.battery_life = battery_life
        self.material = material
        self.revenue = revenue
        self.price = price

#Investment function keeps track of money and the consumer utility
    def investment(self, revenue_change, budget_change):
        self.revenue += revenue_change
        self.budget += budget_change
