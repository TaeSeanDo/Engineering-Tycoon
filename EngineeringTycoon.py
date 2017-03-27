"""
Sean Tierney
Arnob Kabir
main program
"""
from RobotDecisions import robot_code
from MobileDevicesDecisions import Mobile_Devices_Code

ChocoDecision = raw_input("When you were young, you were absolutely obsessed with chocolate. One day, a 7 year old girl came up to you and asked you if she could have some of your chocolate. Do you give her some? (Y/N)").upper
if ChocoDecision == "Y":
    print "You may have less chocolate, but at least someone else could share your passion for chocolate."
if ChocoDecision == "N":
    print "As you told the girl that you would not give her chocolate, her eyes lit up with a burning passion. You may regret this decision in the future, but only time will tell."


print '20 years after the little "Chocolate Incident", you have become a business man and have decided to enter the engineering industry.'
product_choice = raw_input("Do you want to build (1) a mobile device, (2) a robot, or (3) a snowman?")

if product_choice == "1":
    #MD stands for "Mobile Device"
    Mobile_Devices_Code()
elif product_choice == "2":
    robot_code()

elif product_choice == 3:
    print "Do you want to build a snowman?"

else:
    print "That is not a choice"
