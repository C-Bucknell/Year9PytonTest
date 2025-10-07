#Task 9a Snail Cup
'''
Task 9a Snail Cup (8 marks)

You're refereeing a snail race. Sometimes snails curl up and go to sleep 
during races, which disqualifies them.

We've given you a list called racers, which contains the names of the 
snails in the race.

Write a program to help you keep track of the race. It should ask for 
the name of a racer who's gone to sleep and replace their name in the 
list with 'Disqualified'. If that name isn't in the list, it should leave 
the list unmodified and print a message saying all the racers are still awake.

Here's an example of how your program should look:
=========================
And the line up is: Dash, Speedy, Lighting, Flash, Sonic
Who's gone to sleep? Speedy
Speedy has been disqualified!
Remaining racers: Dash, Disqualified, Lighting, Flash, Sonic
========================= 

Here's another example where an inputted name isn't on the list
=========================
And the line up is: Dash, Speedy, Lighting, Flash, Sonic
Who's gone to sleep? Gogo
All snails still awake.
Remaining racers: Dash, Speedy, Lighting, Flash, Sonic
=========================


'''



def main():
    #===============================
    # Write your code for input here
    #==============================
    #And the line up is: Dash, Speedy, Lighting, Flash, Sonic
    racers = input("And the line up is: ")
    racers_list = racers.split(", ")
    sleep_Racer = input("Who's gone to sleep? ")
    if sleep_Racer in racers_list:
        index = racers_list.index(sleep_Racer)
        racers_list[index] = "Disqualified"
        print(f"{sleep_Racer} has been disqualified!")
    else:
        print("All snails still awake.")
        
    print("Remaining racers: " + ", ".join(racers_list))
    
#===============================
# End of your code for input here
#===============================

if __name__ == '__main__':
    main()
