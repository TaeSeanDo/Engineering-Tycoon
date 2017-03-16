"""
Sean Tierney
Robot-production class
"""

class Robot:
    """docstring for Robot"""
    def __init__(self, budget, colors, size, max_speed = 1, cooling_system = 1,  battery_life = 1, consumer_utility = 0, revenue = 0):
        super(Robot, self).__init__()
        self.budget = budget
        self.colors = colors
        self.size =  size
        self.max_speed = max_speed
        self.torque = torque
        self.cooling_system = cooling_system
        self.battery_life = battery_life
        self.consumer_utility = consumer_utility
        self.revenue = revenue
    def investment(self, consumer_utility_change, revenue_change, budget_change):
        self.consumer_utility += consumer_utility_change
        self.revenue += revenue_change
        self.budget += budget_change
    def __str__(self):
        msg = "Your robot is " + size[0] + " x " size[1] " x " + size[2] " and comes in "
        for i in range self.colors.length:
            msg += self.colors[i]
            if i < self.colors.length - 1:
                msg += ", "
            if i == self.colors.length - 2:
                msg += "and "
