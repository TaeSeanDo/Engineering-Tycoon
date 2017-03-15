"""
Sean Tierney
Arnob Kabir
main program
"""
print "OK, so you chose robot"

colors_length = int(raw_input("How many colors should it come in?"))
colors = []
for i in range(colors_length):
    colors.append(raw_input("What other color?"))
length = int(raw_input("What should the length of the robot be?"))
width = int(raw_input("What about the width?"))
height = int(raw_input("The height?"))
size = [length, width, height]
budget = int(raw_input("What is your budget?"))
