"""
Sean Tierney
Robot-production class
"""

class Robot:
    """docstring for Robot"""
    def __init__(self, color, size, value = 0, revenue = 0):
        super(Robot, self).__init__()
        self.color = color
        self.size =  size
        self.value = value
        self.revenue = revenue
    def investment(self, value_increase, revenue_increase):
        self.value += value_increase
        self.revenue += revenue_increase
