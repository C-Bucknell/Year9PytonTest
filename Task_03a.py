#Task 3a Marco Polo
'''
Task 3 Phone charger (4marks)

Write a program that ask the user what percentage of battery power their 
mobile phone has. If the charge remaining is 5% or less, print out Connect 
your charger! For example:
=========================
Remaining charge: 3
Connect your charger!
========================= 
If the charge remaining is more than 5%, the program should do nothing:
=========================
Remaining charge: 50
All good.
========================= 

'''
def main():
  #===============================
  # Write your code for input here
  charge = input("Remaining charge: ")
  if charge > 5:
      print("All good.")
  else:
    print("Connect your charger!")
      

  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
