"""
Sean Tierney
Robot-production class
"""

class Robot:
    """docstring for Robot"""
    def __init__(self, budget, colors, size, max_speed, torque, cooling_YN,  battery_life, consumer_utility = 0, revenue = 0):
        super(Robot, self).__init__()
        self.budget = budget
        self.color = colors
        self.size =  size
        self.max_speed = max_speed
        self.torque = torque
        self.cooling_YN = cooling_YN
        self.battery_life = battery_life
        self.consumer_utility = consumer_utility
        self.revenue = revenue
    def investment(self, consumer_utility_change, revenue_change, budget_change):
        self.consumer_utility += consumer_utility_change
        self.revenue += revenue_change
        self.budget += budget_change
