"""
Sean Tierney
Robot-production class
"""
from math import pow
from ProductClass import Product

class Robot(Product):
    """Class for Robot, inherits Product class"""
    def __init__(self, difficulty, colors, size, max_speed = 1, cooling_system = 1,  battery_life = 1, revenue = 0):
        Product.__init__(self, difficulty, revenue)
        self.difficulty = difficulty
        self.colors = colors
        self.size =  size
        self.max_speed = max_speed
        self.cooling_system = cooling_system
        self.battery_life = battery_life
    def investment(self, max_speed_increase, cooling_system_increase, battery_life_increase, cost):
        self.max_speed += max_speed_increase
        self.cooling_system += cooling_system_increase
        self.battery_life += battery_life_increase
        revenue = 5000 * pow(self.max_speed, 1.0/3) + 3000 * pow(self.cooling_system, 1.0/3) + 8000 * pow(self.battery_life, 1.0/3)
        Product.investment(self, revenue, cost)
    def __str__(self):
        msg = "Your robot is " + str(self.size[0]) + " x " + str(self.size[1]) + " x " + str(self.size[2]) \
                + " and comes in " + str(len(self.colors)) + " colors: "
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
