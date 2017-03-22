"""
Sean Tierney
Arnob Kabir
main program
"""
from RobotProduction import Robot

import MobileDevices
product_choice = str(raw_input("Do you want to build (1) a mobile device, (2) a robot, or (3) a snowman?"))

if product_choice == 1:
    print "Before we can get started with selling your mobile devices, we need to know what sort of features the mobile device has."
    print "Each of these features on your device can affect the outcome of the game, so choose them wisely."
    print "However, to obtain better features, you will need to use more of your budget."
    print "Good luck!"

    #MD stands for "Mobile Device"
    MD_difficulty = -1
    while MD_difficulty > 3 or MD_difficulty < 1:
        MD_difficulty = int(raw_input("First, we have to set the difficulty. Would you like to play on Easy('1', Medium('2'), or Hard('3')?"))
        if MD_difficulty == 1:
            print "Your budget is $600000"
        elif MD_difficulty == 2:
            print "Your budget is $300000"
        elif MD_difficulty == 3:
            print "Your budget is $200000"
        else:
            print "That is not a difficulty choice"

    MD_color = 0
    while  MD_color < 1 or MD_color > 5:
        MD_color = int(raw_input("More colors for a device increases its popularity. \
    However, the more colors you want to produce it in, the more it will cost. \
    Each added color costs $5000.\
    How many colors do you want your product to come in? \
    (minimum is 1, maximum is 5)"))
    MD_processor_proficiency = raw_input('You need a processor for your device. ()')
    MD_internal_storage_capacity = raw_input("Internal storage capacity:")
    MD_headjack_YN = raw_input("Should we have a headjack?")
    MD_battery_life = raw_input("Battery life:")
    MD_material = raw_input("Material:")
    MD_price = raw_input("Price:")

    UserProduct = MobileDevices.mobile_devices(MD_color, MD_processor_proficiency, \
    MD_internal_storage_capacity, MD_headjack_YN, MD_battery_life, \
    MD_material, MD_price)

if product_choice == 2:
    print "OK, so you chose robot"

    colors_length = int(raw_input("How many colors should it come in?"))
    colors = []
    for i in range(colors_length):
        colors.append(raw_input("What other color?"))
    length = int(raw_input("What should the length of the robot be?"))
    width = int(raw_input("What about the width?"))
    height = int(raw_input("The height?"))
    size = [length, width, height]
    difficulty = int(raw_input("What is the difficulty?"))
    robot = Robot(difficulty, colors, size)
    print robot
    print robot.get_budget()
