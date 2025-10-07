#Task 9b Snail Cup
'''
Task 9b Snail Cup (4 marks)

Modify the code from Part a to print out the snails in alphabetical order on separate lines. 

It should ask for the name of a racer who's gone to sleep and REMOVE their name in the list. If 
that name isn't in the list, it should leave the list unmodified and print a message 
saying all the racers are still awake.

Here's an example of how your program should look:
=========================
And the line up is: Dash, Speedy, Lighting, Flash, Sonic
Who's gone to sleep? Dash
Remaining racers:
Flash
Lighting
Sonic
Speedy
========================= 

'''



def main():
    #===============================
    # Write your code for input here
    #==============================
    racers = input("And the line up is: ")
    racers_list = racers.split(", ")
    sorted_racers_list = sorted(racers_list)

    sleep_Racer = input("Who's gone to sleep? ")
    if sleep_Racer in sorted_racers_list:
        racers_list.remove(sleep_Racer)
        index = sorted_racers_list.index(sleep_Racer)
        #Delete the racer from the list
        #my_list.remove(2)  # Removes the first occurrence of 2

        sorted_racers_list[index] = "Disqualified"
        print(f"{sleep_Racer} has been disqualified!")
    else:
        print("All snails still awake.")
        
    print("Remaining racers: ")
    for racers in sorted_racers_list:
        print(racers)
    
#===============================
# End of your code for input here
#===============================

if __name__ == '__main__':
    main()
