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
            decision1 = raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?")
            while (decision1 != '1' and decision1 != '2' and decision1 != '3'):
                decision1 = raw_input("Enter a number between 1 and 3, please.")
            decision1 = int(decision1)
            if decision1 == 1:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 0
                cost = 0
                print "You chose to invest in speed."
            elif decision1 == 2:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 0
                cost = 0
                print "You chose to invest in cooling."
            elif decision1 == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 0
                cost = 0
                print "You chose to invest in battery."

        if i == 1:
            if decision1 == 1:
                decision2 = raw_input("In regard to the speed of your robot, do you want to do make (1) a large investment or (2) a small investment at this time?")
                while (decision2 != '1' and decision2 != '2'):
                    decision2 = raw_input("Enter a number between 1 and 2, please.")
                decision2 = int(decision2)
                if decision2 == 1:
                    max_speed_increase = 3
                    cooling_increase = 0
                    battery_life_increase = 0
                    cost = 60000
                    print "You chose to take a risk."
                elif decision2 == 2 or decision2 == '2':
                    max_speed_increase = 1
                    cooling_increase = 0
                    battery_life_increase = 0
                    cost = 1000
                    print "You chose to play it safe."
            elif decision1 == 2:
                decision2 = raw_input("In regard to the cooling capacity of your robot, do you want to do make (1) a large investment or (2) a small investment at this time?")
                while (decision2 != '1' and decision2 != '2'):
                    decision2 = raw_input("Enter a number between 1 and 2, please.")
                decision2 = int(decision2)
                try:
                    decision2 = int(raw_input("In regard to the cooling capacity of your robot, do you want to do make (1) a large investment  of 6000 or (2) a small investment at this time of 1000?"))
                except:
                    decision2 = raw_input("Enter a number between 1 and 2, please.")
                if decision2 == 2:
                    max_speed_increase = 0
                    cooling_increase = 5
                    battery_life_increase = 0
                    cost = 60000
                    print "You chose to take a risk."
                elif decision2 == 2 or decision2 == '2':
                    max_speed_increase = 0
                    cooling_increase = 2
                    battery_life_increase = 0
                    cost = 1000
                    print "You chose to play it safe."
            elif decision1 == 3:
                decision2 = raw_input("In regard to the cooling capacity of your robot, do you want to do make (1) a large investment or (2) a small investment at this time?")
                while (decision2 != '1' and decision2 != '2'):
                    decision2 = raw_input("Enter a number between 1 and 2, please.")
                decision2 = int(decision2)
                try:
                    decision2 = int(raw_input("In regard to the cooling capacity of your robot, do you want to do make (1) a large investment  of 6000 or (2) a small investment at this time of 1000?"))
                except:
                    decision2 = raw_input("Enter a number between 1 and 2, please.")
                if decision2 == 2:
                    max_speed_increase = 0
                    cooling_increase = 0
                    battery_life_increase = 1
                    cost = 60000
                    print "You chose to take a risk."
                elif decision2 == 2 or decision2 == '2':
                    max_speed_increase = 0
                    cooling_increase = 0
                    battery_life_increase = 2
                    cost = 1000
                    print "You chose to play it safe."

        if i == 2:
            decision1 = raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?")
            while (decision1 != '1' and decision1 != '2' and decision1 != '3'):
                decision1 = raw_input("Enter a number between 1 and 3, please.")
            decision1 = int(decision1)
            if decision == 1 or decision == '1':
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
            decision1 = raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?")
            while (decision1 != '1' and decision1 != '2' and decision1 != '3'):
                decision1 = raw_input("Enter a number between 1 and 3, please.")
            decision1 = int(decision1)
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
        if budget <= 0:
            break;
