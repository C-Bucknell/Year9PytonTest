#Task 6a New Words
'''
Task 6a New Words (4marks)

Write a program to read in a message and give it more emphasis!

Repeat the last letter of the word 5 times, and end with an exclamation 
mark.

You want to ADD THE REPEATS TO THE ORIGINAL WORD, so the last letter will 
appear 6 times in total. Like this, which is typo plus ooooo:

=========================
Say: Oh no, typo
Oh no, typoooooo!
========================= 

Here's another example:
=========================
Say: lol
lollllll!
=========================

If the word ends in a double letter, don't do anything special; you'll 
just end up with 7 of the last letters. For example:
=========================
Say: Yass
Yasssssss!
=========================

'''
def main():
  #===============================
  # Write your code for input here
  input_Word = input("Say: ")
  last_Letter = input_Word[-1]
  new_Word = input_Word + last_Letter * 5 + "!"
  print(new_Word) 

  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
