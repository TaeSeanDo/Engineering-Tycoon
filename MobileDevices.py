#Sets up the class for mobile devices
class mobile_devices:
    def __init__(self, difficulty, colors, processor_type, internal_storage_capacity, \
            headjack_YN, battery_life, material, consumer_utility = 0,\
            revenue = 0,  price = 0):
        self.budget = 600000/difficulty
        self.colors = colors
        self.processor_type = processor_type
        self.internal_storage_capacity = internal_storage_capacity
        self.headjack_YN = headjack_YN
        self.battery_life = battery_life
        self.material = material
        self.consumer_utility = consumer_utility
        self.revenue = revenue
        self.price = price

#Investment function keeps track of money and the consumer utility
    def investment(self, consumer_utility_change, revenue_change, \
    budget_change):
        self.consumer_utility += consumer_utility_change
        self.revenue += revenue_change
        self.budget += budget_change
