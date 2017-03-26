"""
Sean Tierney
Arnob Kabir
main program
"""
from RobotDecisions import robot_code
import MobileDevices

def enter():
    raw_input()

ChocDecision = raw_input("When you were young, you were absolutely obsessed with chocolate. One day, a 7 year old girl came up to you and asked you if she could have some of your chocolate. Do you give her some? (Y/N)").upper
if ChocDecision == "Y":
    print "You may have less chocolate, but at least someone else could share your passion for chocolate."
if ChocDecision == "N":
    print "As you told the girl that you would not give her chocolate, her eyes lit up with a burning passion. You may regret this decision in the future, but only time will tell."

enter()
print '20 years after the little "Chocolate Incident", you have become a business man and have decided to enter the engineering industry.'
enter()
product_choice = raw_input("Do you want to build (1) a mobile device, (2) a robot, or (3) a snowman?")

if product_choice == "1":
    #MD stands for "Mobile Device"
    MD_difficulty = 0
    while MD_difficulty > 3 or MD_difficulty < 1:
        try:
            MD_difficulty = int(raw_input("First, we have to set the difficulty. Would you like to play on Easy('1', Medium('2'), or Hard('3')?"))
        except:
            MD_difficulty = int(raw_input("Try again."))
        if MD_difficulty == 1:
            print "Your budget is $600000"
        elif MD_difficulty == 2:
                print "Your budget is $300000"
        elif MD_difficulty == 3:
            print "Your budget is $200000"
        else:
    		print "That is not a difficulty choice"
        MD_color = 0
    MD_processor_proficiency = 0
    MD_internal_storage_capacity = 0
    MD_headjack_YN = 0
    MD_battery_life = 0
    MD_material = 0
    MD_price = 0
    while  MD_color < 1 or MD_color > 5:
        try:
            MD_color = int(raw_input("More colors for a device increases its popularity. However, the more colors you want to produce it in, the more it will cost. Each added color costs $5000. How many colors do you want your product to come in? (minimum is 1, maximum is 5)"))
        except:
            MD_color = int(raw_input("Try again"))
            if MD_color < 1 or MD_color > 5:
                print "That is not a choice"
    while MD_processor_proficiency < 1 or MD_processor_proficiency > 5:
        try:
            MD_processor_proficiency = int(raw_input('You need a processor for your device. The worst is (1), the best is (5)'))
        except:
            MD_processor_proficiency = int(raw_input('Try again'))
    while MD_internal_storage_capacity < 1 or MD_internal_storage_capacity > 5:
        try:
            MD_internal_storage_capacity = int(raw_input("1-5 capacity"))
        except:
            MD_internal_storage_capacity = int(raw_input("Try again"))
    while MD_headjack_YN < 1 or MD_headjack_YN > 2:
        try:
            MD_headjack_YN = int(raw_input("Should we have a headjack?"))
        except:
            MD_headjack_YN = int(raw_input("Try again"))
    while MD_battery_life < 1 or MD_battery_life > 10:
        MD_battery_life = int(raw_input("Battery life (1 to 10 hours)"))
    while MD_material < 1 or MD_material > 3:
        MD_material = int(raw_input("Material:"))
    MD_price = int(raw_input("Price:"))

    UserProduct = MobileDevices.mobile_devices(MD_color, MD_processor_proficiency, MD_internal_storage_capacity, MD_headjack_YN, MD_battery_life, MD_material, MD_price)

elif product_choice == "2":
    robot_code()

elif product_choice == 3:
    print "Do you want to build a snowman?"

else:
    print "That is not a choice"

"""
        if i == 3:
            decision = raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?")
            while (decision != '1' and decision != '2' and decision != '3'):
                decision = raw_input("Enter a number between 1 and 3, please.")
            decision = int(decision)
            if decision == 1:
                max_speed_increase = 1
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                cooling_increase = 1
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."
        if i == 4:
            decision = raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?")
            while (decision != '1' and decision != '2' and decision != '3'):
                decision = raw_input("Enter a number between 1 and 3, please.")
            decision = int(decision)
            if decision == 1:
                max_speed_increase = 1
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                cooling_increase = 1
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."
"""
