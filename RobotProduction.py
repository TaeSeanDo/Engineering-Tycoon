"""
Sean Tierney
Robot-production class
"""

class Robot:
    """docstring for Robot"""
    def __init__(self, difficulty, colors, size, max_speed = 1, cooling_system = 1,  battery_life = 1, consumer_utility = 0, revenue = 0):
        self.budget = 600 / difficulty
        self.colors = colors
        self.size =  size
        self.max_speed = max_speed
        self.cooling_system = cooling_system
        self.battery_life = battery_life
        self.consumer_utility = consumer_utility
        self.revenue = revenue
    def investment(self, consumer_utility_change, revenue_change, budget_change):
        self.consumer_utility += consumer_utility_change
        self.revenue += revenue_change
        self.budget += budget_change
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
        return msg
