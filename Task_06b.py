#Task 6b New Words
'''
Task 6b New Words - Part2 (4marks)

Add to the code from part 1 to create another new word. 
The new word should replace 'o' in the word with a 'y'. 
Use a for loop to print out each letter of this new word on a new line. 
Then print this new word on 1 line at the end.

For example:
=========================
Say: typo
New word!
t
y
p
y
y
y
y
y
y
typyyyyyy!
========================= 

'''
def main():
  #===============================
  # Write your code for input here
  input_Word = input("Say: ")
  #replace o with y
  new_Word_o_to_y = input_Word.replace('o', 'y')
  last_Letter = new_Word_o_to_y[-1]
  new_word_With_Extras = new_Word_o_to_y + last_Letter* 5
  print("New word!")
  for letter in new_word_With_Extras:
        print(letter)
  print(new_word_With_Extras + '!')

  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
