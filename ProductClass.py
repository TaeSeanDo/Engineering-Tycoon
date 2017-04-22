
"""
Sean Tierney
Product class
"""

class Product:
    """superclass for robot, mobile devices, and snowman"""
    def __init__(self, difficulty, revenue):
        self.difficulty = difficulty
        self.budget = 30000 / difficulty
        self.revenue = revenue
    def investment(self, revenue, budget_decrease):
        self.revenue = revenue
        self.budget -= budget_decrease
    def __str__(self, stat_msgs, stats):
        if len(stat_msgs) != len(stats):
            msg = "\n!!!!!!!!!!!!!!!!\n"
            msg += "ERROR: len(stat_msgs) = len(stats) is false."
        else:
            msg = '\n'
            for stat_index in range (len(stats)):
                msg += '\n\t'
                msg += stat_msgs[stat_index] + ': '
                msg += str(stats[stat_index])
            msg += "\n\n\tDifficulty: " + str(self.difficulty)
            msg += "\n\tBudget: " + str(self.budget)
            msg += "\n\tRevenue: " + str(self.revenue) + '\n'
        return msg
