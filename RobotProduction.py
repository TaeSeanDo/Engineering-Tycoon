"""
Sean Tierney
Robot-production class
"""

from ProductClass import Product

class Robot(Product):
    """Class for Robot, inherits Product class"""
    def __init__(self, difficulty, colors, size, max_speed = 1, cooling_system = 1,  battery_life = 1, revenue = 0):
        Product.__init__(self, difficulty, revenue)
        self.colors = colors
        self.size =  size
        self.max_speed = max_speed
        self.cooling_system = cooling_system
        self.battery_life = battery_life
    def investment(self, max_speed_increase, cooling_increase, battery_life_increase, cost):
        self.max_speed += max_speed_increase
        self.cooling_system += cooling_increase
        self.battery_life += battery_life_increase
        revenue_change = max_speed_increase * 10000 + cooling_increase * 1000 + battery_life_increase + 50000
        Product.investment(self, revenue_change, cost)


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
        msg += '.'
        msg
        return msg
