#Task 2b Marco Polo
'''
Task 2 Marco Polo (2marks)
Part b

Modify the code from part 1 to accept any variation of Marco capitalised. 

For example, the program should work for lower case (marco) or mixed case (mArcO)

Your program should work like this when you say Marco!:
=========================
Text: marco!
Polo!
========================= 
=========================
Text: mArCo!
Polo!
========================= 

'''
def main():
  #===============================
  # Write your code for input here
  text = input("Text: ")
  if text.lower() == "marco!":
    print("Polo!")    


  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
