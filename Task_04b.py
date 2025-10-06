#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
def main():
  #===============================
  # Write your code for input here
  age = input("How old are you? ")
  if age > 100:
      years_Until_letter = age - 100
      print(f'You already got your letter {years_Until_letter} years ago')
  else:
      years_Until_letter = 100 - age
      print("Years until your letter...")
      print(years_Until_letter)    

  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
