from RobotProduction import Robot
import random

def robot_code(player_is_generous):
    print "OK, so you chose to build a robot."
    print

    print "First, you should decide on the color(s) the robot should come in."
    while True:
        try:
            colors_length = int(raw_input("How many colors should it come in? (Enter a number between 1 and 5)\n"))
        except:
            print "Please enter an integer between 1 and 5.\n"
            continue
        else:
            if colors_length >= 1 and colors_length <= 5:
                break
    colors = []
    for i in range(colors_length):
        if i == 0 and colors_length == 1:
            #runs if there is only one color
            next_color = raw_input("What color should the robot come in?\n")
        elif i == 0:
            #runs if there is more than one color and user is inputting the first one
            next_color = raw_input("Enter one of the colors the robot should come in:\n")
        else:
            #runs if the user is inputting colors that are not the first color
            next_color = raw_input("What other color?\n")
        colors.append(next_color)

    print "\nYou should also decide the physical parameters of the robot."
    while True:
        try:
            height = int(raw_input("What should the height of the robot be in inches?\n"))
        except:
            print "Please enter a positive integer.\n"
            continue
        else:
            if height > 0:
                break
    while True:
        try:
            length = int(raw_input("What about the length?\n"))
        except:
            print "Please enter a positive integer.\n"
            continue
        else:
            if length > 0:
                break
    while True:
        try:
            width = int(raw_input("The width?\n"))
        except:
            print "Please enter a positive integer.\n"
            continue
        else:
            if width > 0:
                break
    size = [length, width, height]

    print "Your difficulty determines your starting budget as well as your overall luck when making decisions."
    while True:
        try:
            difficulty = int(raw_input("What is the difficulty --> (1) BEGINNER, (2) EASY, (3) MEDIUM, (4) HARD, OR (5) EXPERT?\n"))
        except:
            print "Please enter a whole number between 1 and 5.\n"
            continue
        else:
            if difficulty >= 1 and difficulty <= 5:
                break
    robot = Robot(difficulty, colors, size)

    print robot


    decision_num = 6
    for i in range (decision_num):
        max_speed_increase = 0
        cooling_increase = 0
        battery_life_increase = 0
        cost = 0

        if i == 0:
            print "The best way to earn a profit is to invest in your product."
            decision1 = raw_input("Would you like to invest in (1) the speed of your robot, (2) your cooling system, or (3) the battery life?\n")
            while (decision1 != '1' and decision1 != '2' and decision1 != '3'):
                decision1 = raw_input("Enter a whole number between 1 and 3, please.\n")
            decision1 = int(decision1)
            if decision1 == 1:
                print "You chose to invest in speed.\n"
            elif decision1 == 2:
                print "You chose to invest in cooling.\n"
            elif decision1 == 3:
                print "You chose to invest in battery.\n"

        if i == 1:
            max_speed_increase = 0
            cooling_increase = 0
            battery_life_increase = 0
            decision2 = raw_input("Do you want to do make (1) a small investment of $1000 or (2) a large investment of $6000 at this time?\n")
            while (decision2 != '1' and decision2 != '2'):
                decision2 = raw_input("Enter 1 or 2.\n")
            decision2 = int(decision2)
            if decision2 == 1:
                cost = 1000
            else:
                cost = 6000
            if decision2 == 1:
                if decision1 == 1:
                    max_speed_increase = 1
                elif decision1 == 2:
                    cooling_increase = 2
                elif decision1 == 3:
                    battery_life_increase = 1
                cost = 1000
                print "You chose to play it safe.\n"
            elif decision2 == 2:
                if decision1 == 1:
                    max_speed_increase = 3
                elif decision1 == 2:
                    cooling_increase = 5
                elif decision1 == 3:
                    battery_life_increase = 2
                cost = 6000
                print "You chose to take a risk.\n"

        if i == 2:
            print "All great feats of engineering were accomplished through extensive research, though research does not always work."
            print "The cost of this research is $10000."
            decision3 = raw_input("Would you like to conduct research on your product? (Y/N)\n").upper()
            while (decision3 != 'Y' and decision3 != 'N'):
                decision3 = raw_input("Enter Y or N, please.\n").upper()
            if decision3 == 'Y':
                research = True
                print "You chose to research for your robot.\n"
                cost = 10000
            else:
                research = False
                print "You chose not to research for your robot.\n"
                cost = 0
            if research:
                research_rand_num = random.randint(1, 10)
                if (robot.difficulty == 1 and research_rand_num <= 7) or (robot.difficulty == 2 and research_rand_num <= 5) or (robot.difficulty == 3 and research_rand_num <= 3):
                    research_success = True
                else:
                    research_success = False
                if research_success:
                    max_speed_increase = 3
                    cooling_increase = 3
                    battery_life_increase = 3

        if i == 3:
            print "A new battery just entered the market. This battery is 3 times lighter than the original battery and it holds a charge for twice as long."
            print "However, transitioning to this battery will cost $5000"
            decision4 = raw_input("Do you want to use this battery? (Y/N)").upper()
            while decision4 != 'Y' and decision4 != 'N':
                decision4 = raw_input("Type 'Y' or 'N'").upper()
            if decision4 == 'Y':
                max_speed_increase = 1
                battery_life_increase = 3
                cost = 5000
                print "You made your robot faster and your battery life longer."

        if i == 4:
            print "A new method for increasing the speed of your robot has been discovered."
            print "However, using this method for your robot may cause it to overheat slightly and incorporating it into your engineering process will cost $3500."
            decision4 = raw_input("Do you want to use this method in your process? (Y/N)").upper()
            while decision4 != 'Y' and decision4 != 'N':
                decision4 = raw_input("Type 'Y' or 'N'").upper()
            if decision4 == 'Y':
                max_speed_increase = 4
                cooling_increase = -1
                cost = 3500
                print "You are now using the new method and your robot is faster as a result."
            if robot.budget > 0:
                print "\nCongratulations, you made it through the entire game without spending your entire budget."
                print "You officially deserve the \"Cheapskate Award.\""
                break


        robot.investment(max_speed_increase, cooling_increase, battery_life_increase, cost)
        if robot.budget <= 0:
            print "Your budget dropped to $0"
            break

        show_stats = raw_input("Show stats? (Y/N)").upper()
        while show_stats != 'Y' and show_stats != 'N':
            show_stats = raw_input("Type 'Y' or 'N'").upper()
        if show_stats == 'Y':
            print robot

    print "BREAKING NEWS!!!"
    print "There is new fierce competitor in the robot market: Stacy Botson."
    print "When researching her, your ",
    if player_is_generous:
        print "face lights up "
    else:
        print "heart sinks "
    print "when you recognize her as the girl you saw in the fields almost 20 years ago."
    print "Once this woman discovers that you are in the marketplace, ",
    if player_is_generous:
        print "she jumps on the chance to help you out with your robot."
        print "She even offers to merge your and her firms together. You accept, of course." #Allow the player to decide
        print "This creates a boom in your revenue, the like of which you have never seen before!"
        max_speed_increase = 5
        cooling_increase = 5
        battery_life_increase = 5
    else:
        print "she rapidly hunts you down to crush your chances in the marketplace."
        print "It's too bad she holds grudges."
        max_speed_increase = -5
        cooling_increase = -5
        battery_life_increase = -5

    final_stats_continue = raw_input("\n\nPress enter to continue.\n")
    robot.investment(max_speed_increase, cooling_increase, battery_life_increase, cost)

    #the good, the bad, and the ugly
    print "\nYour final stats are: \n"
    print robot
    if robot.revenue < 30000:
        print "Your robot is kinda pathetic, I'm not gonna lie. You will live the rest of your life in debt and poverty.\nBetter luck next time!"
    elif robot.revenue >= 30000 and robot.revenue < 60000:
        print "Your robot sold pretty well and you made a decent profit."
    else:
        print "Your robot was a serious competitor in the robot industry and it caused you to draw extreme profits. \nCongratulations!"
