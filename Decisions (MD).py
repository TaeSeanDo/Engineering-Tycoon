import EngineeringTycoon
#Decisions for the Mobile Devices branch

def mobile_devices_function():

    print "20 years after the little 'chocolate incident', you decided to enter the mobile device manufacturing business."
    enter()
    decision_num = 5
    for i in range(decision_num):
            if i == 0:
                decision = ''
                while decision != '1' or decision != '2' or decision != '3':
                    decision = raw_input("Let's start with some investing! By investing in different attributes of your device, you can increase your revenue (for a price, of course). Would you like to invest in (1) the internal storage capacity ($2000), (2) processor profiency ($3000), or (3) the battery life ($4000) of the mobile device?")
                    if decision == "1":
                        internal_storage_capacity_increase = 1
                        processor_proficiency_increase_increase = 0
                        battery_life_increase = 0
                        cost = 2000
                        print "You chose to invest in internal storage."
                    elif decision == "2":
                        internal_storage_capacity_increase = 0
                        processor_proficiency_increase = 1
                        battery_life_increase = 0
                        cost = 3000
                        print "You chose to invest in processor speed."
                    elif decision == "3":
                        internal_storage_capacity_increase = 0
                        processor_proficiency_increase = 0
                        battery_life_increase = 1
                        cost = 4000
                        print "You chose to invest in battery life."


            if i == 1:
                    decision = raw_input("Would you like to research (press '1' for choices, press '0' to not research anything)?")
                if decision == 1:
                    print "Here is what you can research:\n\n|  Item  | price |Success rate|\n|Projector |$4000|30%|"




            if i == 2:
                decision = int(raw_input())

                if decision == 1:
                    internal_storage_capacity_increase = 1
                    processor_proficiency_increase = 0
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in internal storage."
                elif decision == 2:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 1
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in processor speed."
                elif decision == 3:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 0
                    battery_life_increase = 1
                    cost = 5000
                    print "You chose to invest in battery."

            if i == 3:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the internal storage capacity, (2) processor profiency, or (3) the battery life of the mobile device?"))
                decision = int(raw_input("Put a number, please."))
                if decision == 1:
                    internal_storage_capacity_increase = 1
                    processor_proficiency_increase = 0
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in internal storage."
                elif decision == 2:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 1
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in processor speed."
                elif decision == 3:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 0
                    battery_life_increase = 1
                    cost = 5000
                    print "You chose to invest in battery."

            if i == 4:
                decision = int(raw_input("The best way to earn a profit is to invest in your product. Would you like to invest in (1) the internal storage capacity, (2) processor profiency, or (3) the battery life of the mobile device?"))
                decision = int(raw_input("Put a number, please."))
                if decision == 1:
                    internal_storage_capacity_increase = 1
                    processor_proficiency_increase = 0
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in internal storage."
                elif decision == 2:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 1
                    battery_life_increase = 0
                    cost = 2000
                    print "You chose to invest in processor speed."
                elif decision == 3:
                    internal_storage_capacity_increase = 0
                    processor_proficiency_increase = 0
                    battery_life_increase = 1
                    cost = 5000
                    print "You chose to invest in battery."

mobile_devices_function()
