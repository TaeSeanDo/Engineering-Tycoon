"""
Sean Tierney
Arnob Kabir
main program
"""
import RobotProduction
import MobileDevices

product_choice = 0
while product_choice > 2 or product_choice < 1:
    try:
        product_choice = int(raw_input("Would you like to run a (1) robot factory or a (2)mobile device production company?"))
    except:
        product_choice = int(raw_input("Try again."))
    if product_choice == 1:
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
        robot = RobotProduction.Robot(difficulty, colors, size)
        print robot

        print "Before we can get started with selling your mobile devices, we need to know what sort of features the mobile device has."
        print "Each of these features on your device can affect the outcome of the game, so choose them wisely."
        print "However, to obtain better features, you will need to use more of your budget."
        print "Good luck!"

    elif product_choice == 2:
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
    else:
        print "That is not a choice"
