from math import log10
from ProductClass import Product
#Sets up the class for mobile devices
class mobile_devices(Product):
    def __init__(self, difficulty, colors, headjack_YN, material, battery_life_MD=1, processor_proficiency=1, internal_storage_capacity=1, revenue=0):
        Product.__init__(self, difficulty, revenue)
        self.difficulty = difficulty
        self.colors = colors
        self.headjack_YN = headjack_YN
        self.battery_life_MD = battery_life_MD
        self.material = material
        self.processor_proficiency = processor_proficiency
        self.internal_storage_capacity = internal_storage_capacity
        self.set_stats()

    #Investment function keeps track of money
    def investment(self, internal_storage_capacity_increase, processor_proficiency_increase, battery_life_MD_increase, cost):
        self.internal_storage_capacity += internal_storage_capacity_increase
        self.processor_proficiency += processor_proficiency_increase
        self.battery_life_MD += battery_life_MD_increase
        self.internal_storage_capacity = max(self.internal_storage_capacity, 1)
        self.processor_proficiency = max(self.processor_proficiency, 1)
        self.battery_life_MD = max(self.battery_life_MD, 1)
        revenue = 3000 * log10(self.internal_storage_capacity) + 1800 * log10(self.processor_proficiency) + 4800 * log10(self.battery_life_MD)
        Product.investment(self, revenue, cost)

    def set_stats(self):
        self.stats = [self.internal_storage_capacity, self.processor_proficiency, self.battery_life_MD]

    def __str__(self):
        if self.headjack_YN == 'Y':
            HeadjackMsg = "does have"
        elif self.headjack_YN == 'N':
            HeadjackMsg = "does not have"
        if self.material == '1':
            MaterialMsg = 'tin'
        elif self.material == '2':
            MaterialMsg = 'aluminum'
        elif self.material == '3':
            MaterialMsg = 'iron'
        msg = "Your mobile device comes in " + str(self.colors) + " colors. It " + HeadjackMsg + " a headjack. It is made of " + MaterialMsg + ".\n"
        stat_msgs = ["Internal storage capacity", "Processor proficiency", "Battery life in hours"]
        self.set_stats()
        msg += Product.__str__(self, stat_msgs, self.stats)
        return msg
