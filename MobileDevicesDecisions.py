#Decisions for the Mobile Devices branch
from MobileDevices import mobile_devices
import random

def Mobile_Devices_Code(player_is_generous):

    print "20 years after the little 'chocolate incident', you decided to enter the mobile device manufacturing business."

    MD_difficulty = ''
    MD_color = ''
    MD_headjack_YN = ''
    MD_material = ''
    while MD_difficulty != '1' or MD_difficulty != '2' or MD_difficulty != '3':
            MD_difficulty = str(raw_input("First, we have to set the difficulty. Would you like to play on Easy(1), Medium(2), or Hard(3)?"))
            if MD_difficulty == '1':
                print "Your budget is $600000"
                MD_difficulty = int(MD_difficulty)
                break
            elif MD_difficulty == '2':
                print "Your budget is $300000"
                MD_difficulty = int(MD_difficulty)
                break
            elif MD_difficulty == '3':
                print "Your budget is $200000"
                MD_difficulty = int(MD_difficulty)
                break
            else:
                print "That is not a difficulty choice"
    while  MD_color != "1" or MD_color != "2" or MD_color != "3" or MD_color != "4" or MD_color != "5":
            MD_color = str(raw_input("More colors for a device increases its popularity. However, the more colors you want to produce it in, the more it will cost. Each added color costs $5000. How many colors do you want your product to come in? (minimum is 1, maximum is 5)"))
            if MD_color == "1" or MD_color == "2" or MD_color == "3" or MD_color == "4" or MD_color == "5":
                break
            print "That is not a choice"

    while MD_headjack_YN != 'Y' or MD_headjack_YN != 'N':
            MD_headjack_YN = str(raw_input("Should it have a headjack? (Y/N)")).upper()
            if MD_headjack_YN == 'Y' or MD_headjack_YN == 'N':
                break
            if MD_headjack_YN != 'Y' or MD_headjack_YN != 'N':
                print "That is not a choice"
    while MD_material != '1' or MD_material != '2' or MD_material != '3':
        MD_material = raw_input("Lastly, we have to decide what your phone is to be made of. Would you like it to be made of (1) tin, (2) aluminum, or (3) iron?")
        if MD_material == '1' or MD_material == '2' or MD_material == '3':
            break
        if MD_material != '1' or MD_material != '2' or MD_material != '3':
            print "That is not a choice."


    UserProduct = mobile_devices(MD_difficulty, MD_color, MD_headjack_YN, MD_material)
    print UserProduct

    decision_num = 4
    for i in range(decision_num):
            if i == 0:
                decision = ''
                while decision != '1' or decision != '2' or decision != '3':
                    decision = raw_input("Let's start with some investing! By investing in different attributes of your device, you can increase your revenue (for a price, of course). Would you like to invest in (1) the internal storage capacity ($2000), (2) processor profiency ($3000), or (3) the battery life ($4000) of the mobile device?")
                    if decision == "1":
                        internal_storage_capacity_increase = 1
                        processor_proficiency_increase_increase = 0
                        battery_life_MD_increase = 0
                        cost = 2000
                        break
                        print "You chose to invest in internal storage."
                    elif decision == "2":
                        internal_storage_capacity_increase = 0
                        processor_proficiency_increase = 1
                        battery_life_MD_increase = 0
                        cost = 3000
                        break
                        print "You chose to invest in processor speed."
                    elif decision == "3":
                        internal_storage_capacity_increase = 0
                        processor_proficiency_increase = 0
                        battery_life_MD_increase = 1
                        cost = 4000
                        break
                        print "You chose to invest in battery life."


            if i == 1:
                while decision != 'Y' or decision != 'N':
                    decision = str(raw_input("The greatest people create new innovations through extensive research. However, research does not always produce results. It costs $10000 to research. Do you want to take the risk? (Y/N)")).upper()
                    if decision == 'Y':
                        print "You decided to research."
                        cost = 10000
                        research_rand_num = random.randint(1, 10)
                        if (UserProduct.difficulty == 1 and research_rand_num <= 7) or (UserProduct.difficulty == 2 and research_rand_num <= 5) or (UserProduct.difficulty == 3 and research_rand_num <= 3):
                            research_success = True
                        else:
                            research_success = False
                        if research_success:
                            internal_storage_capacity_increase = 3
                            processor_proficiency_increase = 3
                            battery_life_MD_increase = 3
                        break
                    elif decision == 'N':
                        print "You decided not to research."
                        cost = 0
                        break



            if i == 2:
                while decision != 'Y' or decision != 'N':
                    decision = raw_input("A smaller, more efficient battery is now on the market. By switching to it, you can have more room for internal storage. However, switching to it costs $5000. Do you switch? (Y/N)").upper()
                    if decision == 'Y':
                        print "You chose to switch."
                        internal_storage_capacity_increase = 1
                        battery_life_MD_increase = 1
                        cost = 5000
                        break
                    elif decision == 'N':
                        print "You decided not to switch"
                        cost = 0
                        break
                    else:
                        print "Enter 'Y' or 'N'."


            if i == 3:
                while decision != 'Y' or decision != 'N':
                    decision = raw_input("A new smaller, and faster processor is now on the market. Switching to it will allow you to add more internal storage to the phone. However, it will cost $5000. Do you want to switch? (Y/N)").upper()
                    if decision == 'Y':
                        internal_storage_capacity_increase = 1
                        processor_proficiency_increase = 1
                        cost = 5000
                        break
                        print "You chose to swtich."
                    elif decision =='N':
                        print "You chose not to switch"
                        cost = 0
                        break
                if UserProduct.budget > 0:
                    print "\nCongratulations, you made it through the entire game without spending your entire budget."
                    print "You officially deserve the \"Cheapskate Award.\""


            UserProduct.investment(internal_storage_capacity_increase, processor_proficiency_increase, battery_life_MD_increase, cost)
            if UserProduct.budget <= 0:
                print "Your budget dropped to $0"
                break

            show_stats = raw_input("Show stats? (Y/N)").upper()
            while show_stats != 'Y' and show_stats != 'N':
                show_stats = raw_input("Type 'Y' or 'N'").upper()
            if show_stats == 'Y':
                print UserProduct


    print "BREAKING NEWS!!!"
    print "There is new fierce competitor in the market for mobile devices and she's no phoney: Jenny Ringman."
    print "When researching her, your ",
    if player_is_generous:
        print "face lights up "
    else:
        print "heart sinks "
    print "when you recognize her as the girl you saw in the fields almost 20 years ago."
    print "Once this woman discovers that you are in the marketplace, ",
    if player_is_generous:
        print "she jumps on the chance to help you out with your mobile device."
        print "She even offers to merge your and her firms together. You accept, of course." #Allow the player to decide
        print "This creates a boom in your revenue, the like of which you have never seen before!"
        internal_storage_capacity_increase = 5
        processor_proficiency_increase = 5
        battery_life_MD_increase = 5
    else:
        print "she rapidly hunts you down to crush your chances in the marketplace."
        print "It's too bad she holds grudges."
        internal_storage_capacity_increase = -5
        processor_proficiency_increase = -5
        battery_life_increase = -5

    UserProduct.investment(internal_storage_capacity_increase, processor_proficiency_increase, battery_life_MD_increase, cost)

    print "\nYour final stats are: \n"
    print UserProduct
    if UserProduct.revenue < 15000:
        print "Your phone is kinda pathetic, I'm not gonna lie. You will live the rest of your life in debt and poverty.\nBetter luck next time!"
    elif UserProduct.revenue >= 15000 and UserProduct.revenue < 30000:
        print "Your phone sold pretty well and you made a decent profit."
    else:
        print "Your phone was a serious competitor in the phone industry and it caused you to draw extreme profits. \nCongratulations!"
