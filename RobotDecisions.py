from RobotProduction import Robot
def robot_code():
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




    decision_num = 5
    for i in range (decision_num):
        if i == 0:
            try:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision = int(raw_input("Put a number, please."))
            if decision == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."

        if i == 1:
            try:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision = (raw_input("Put a number, please."))
            if decision == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."

        if i == 2:
            try:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision = int(raw_input("Put a number, please."))
            if decision == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."

        if i == 3:
            try:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision = int(raw_input("Put a number, please."))
            if decision == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000  
                print "You chose to invest in cooling."
            elif decision == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."

        if i == 4:
            try:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision = int(raw_input("Put a number, please."))
            if decision == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in speed."
            elif decision == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000
                print "You chose to invest in cooling."
            elif decision == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
                print "You chose to invest in battery."

        robot.investment(max_speed_increase, cooling_increase, battery_life_increase, cost)
        show_stats = str(raw_input("Show stats? (Y/N)"))
        while show_stats != 'Y' and show_stats != 'N':
            show_stats = str(raw_input("Type 'Y' or 'N'"))
        if show_stats == 'Y':
            print robot
