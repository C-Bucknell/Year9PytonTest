
#Task 1b More Echos
'''
Task 1 More Echo (2marks)
Part b

Add to the code from part 1 to print out the echo on a separate line. Your program should work like this:
=========================
Shout: hello
hello hello hello

hello
hello
hello
=========================  
'''
def main():
  #===============================
  # Write your code for input here
  var = input('Shout: ')
  print(f'{var} {var} {var}')
  print()
  for i in range(0,3):
          print(var)
  # End of your code for input here
  #===============================

if __name__ == '__main__':
    main()
