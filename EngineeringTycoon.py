"""
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
LIST OPPORTUNITIES IN ERROR LOG!!!!!!!!!!!!!
Sean Tierney
Arnob Kabir
main program
"""
from RobotDecisions import robot_code
from MobileDevicesDecisions import Mobile_Devices_Code

print
print "                   =================="
print "                   |   ENGINEERING  |"
print "                   |     TYCOON     |"
print "                   =================="
print

game_start = raw_input("Press enter to start\n")

chocolate_decision = raw_input("\nYou are a carefree little boy absolutely obsessed with chocolate. As you prance through the fields, you come across a 7 year old girl bereft of chocolate induced satisfaction. You realize that you have so much chocolate that you may not finish it all. Do you offer her some? (Y/N)\n").upper()
while (chocolate_decision != 'Y' and chocolate_decision != 'N'):
    chocolate_decision = raw_input("Enter Y or N, please.\n").upper()
if chocolate_decision == "Y":
    print "You may have less chocolate, but it fills you with joy to know that you did the right thing."
    player_is_generous = True
if chocolate_decision == "N":
    print "As you told the girl that you would not give her chocolate, her eyes lit up with a burning passion. You may regret this decision in the future, but only time will tell."
    player_is_generous = False

print "\n\n20 YEARS LATER...\n"
print "You are now fresh out of college and you have decided to enter the world of engineering."
print "Your first decision is what type of product to make."
play_game = 'Y'
while play_game == 'Y':
    try:

        product_choice = int(raw_input("Do you want to build (1) a mobile device or (2) a robot?\n"))
    except:
        print "\nPlease enter a number\n."
        continue

    if product_choice == 1:
        #MD stands for "Mobile Device"
        Mobile_Devices_Code(player_is_generous)

    elif product_choice == 2:
        robot_code(player_is_generous)

    else:
        continue

    play_game = raw_input("\nDo you want to play again? (Y/N)\n").upper()
    while (play_game != 'Y' and play_game != 'N'):
        play_game = raw_input("Enter Y or N, please.\n")
