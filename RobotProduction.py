"""
Sean Tierney
Robot-production class
"""
from math import log10
from ProductClass import Product

#Sets up the class for mobile devices
class Robot(Product):
    """Class for Robot, inherits Product class"""
    def __init__(self, difficulty, colors, size, max_speed=1, cooling_system=1,  battery_life=1, revenue=0):
        Product.__init__(self, difficulty, revenue)
        self.difficulty = difficulty
        self.colors = colors
        self.size = size
        self.max_speed = max_speed
        self.cooling_system = cooling_system
        self.battery_life = battery_life
        self.set_stats()

    #Investment function keeps track of money
    def investment(self, max_speed_increase, cooling_system_increase, battery_life_increase, cost):
        self.max_speed += max_speed_increase
        self.cooling_system += cooling_system_increase
        self.battery_life += battery_life_increase
        self.max_speed = max(self.max_speed, 1)
        self.cooling_system = max(self.cooling_system, 1)
        self.battery_life = max(self.battery_life, 1)
        revenue = 3000 * log10(self.max_speed) + 1800 * log10(self.cooling_system) + 4800 * log10(self.battery_life)
        Product.investment(self, revenue, cost)

    def set_stats(self):
        self.stats = [self.max_speed, self.cooling_system, self.battery_life]

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
        stat_msgs = ["Maximum speed in meters/sec", "Cooling system proficiency", "Battery life in hours"]
        self.set_stats()
        msg += Product.__str__(self, stat_msgs, self.stats)
        return msg
