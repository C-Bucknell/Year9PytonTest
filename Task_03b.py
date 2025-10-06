#Task 3b Phone charger
'''
Task 3b Phone charger (2marks)

Add to the code from part 1 to include another decision and output. 
That is, if the charge remaining is between 5% and 50%, your program 
should output You should charge your phone soon! For example:
=========================
Remaining charge: 40
You should charge your phone soon!
========================= 

'''
def main():
  #===============================
  # Write your code for input here
  charge = input("Remaining charge: ")
  if charge > 50:
      print("All good.")
  elif charge > 5:
      print("You should charge your phone soon!")
  else:
      print("Connect your charger!")
      

  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
