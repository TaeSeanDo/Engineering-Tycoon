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

    print "The best way to earn a profit is to invest in your product. Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?"
