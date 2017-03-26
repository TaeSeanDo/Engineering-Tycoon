#Sets up the class for mobile devices
from math import log10
from ProductClass import Product
class mobile_devices(Product):
    def __init__(self, difficulty, colors, headjack_YN, battery_life_MD = 1, material, processor_proficiency = 1, internal_storage_capacity = 1, revenue = 0):
        self.difficulty
        self.colors = colors
        self.headjack_YN = headjack_YN
        self.battery_life_MD = battery_life_MD
        self.material = material

#Investment function keeps track of money
    def investment(self, internal_storage_capacity_increase, processor_proficiency_increase, battery_life_MD_increase, cost):
        self.internal_storage_capacity += internal_storage_capacity_increase
        self.processor_proficiency += processor_proficiency_increase
        self.battery_life_MD += battery_life_MD_increase
        revenue = 3000 * log10(self.internal_storage_capacity) + 1800 * log10(self.processor_proficiency) + 4800 * log10(self.battery_life_MD)

    def __str__(self):
        msg = "Your  mobile device comes in " + str(self.colors) + " colors. It "

"""
Sean Tierney
Robot-production class
"""
from math import log10
from ProductClass import Product

    def __str__(self):
        msg = "Your robot is " + str(self.size[0]) + " x " + str(self.size[1]) + " x " + str(self.size[2]) + " and comes in " + str(len(self.colors)) + " color"
        if len(self.colors) != 1:
            msg += 's'
        msg += ': '
        for i in range (len(self.colors)):
            msg += self.colors[i]
            if len(self.colors) == 2:
                if i == 0:
					msg += " and "
            else:
                if i < len(self.colors) - 1:
                    msg += ", "
                if i == len(self.colors) - 2:
                    msg += "and "
        msg += ". \n\n\tMaximum speed in meters/sec: " + str(self.max_speed)
        msg += "\n\tCooling system proficiency: " + str(self.cooling_system)
        msg += "\n\tBattery life in hours: " + str(self.battery_life)
        msg += "\n\n\tDifficulty: " + str(self.difficulty)
        msg += "\n\tBudget: " + str(self.budget)
        msg += "\n\tRevenue: " + str(self.revenue) + '\n'
        return msg
