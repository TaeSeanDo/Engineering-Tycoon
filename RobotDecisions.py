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




    decision_num = 10
    for i in range decision_num:
        if i == 0:
            try:
                decision1 = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"))
            except:
                decision1 = int(raw_input("Put a number, please."))
            if decision1 == 1:
                max_speed_increase = 1
                cooling_increase = 0
                battery_life_increase = 0
                cost = 2000
            elif decision1 == 2:
                max_speed_increase = 0
                cooling_increase = 1
                battery_life_increase = 0
                cost = 2000
            elif decision1 == 3:
                max_speed_increase = 0
                cooling_increase = 0
                battery_life_increase = 1
                cost = 5000
            robot.investment(max_speed_increase, cooling_increase, battery_life_increase, cost)
