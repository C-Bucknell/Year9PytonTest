#Task 7 Debugging
'''
Task 7 Debugging (8marks)

The following code uses a function hello to return Hello 
and your name. This code currently has some errors and needs 
to be debugged to work properly.

This is how it is meant to work
=========================
What is your name? Ben
Your name is too short
========================= 

Another example:
=========================
What is your name? Charlie
Hello, Charlie
=========================

Without removing the function "hello" debug the code so the 
tests above produce the given outputs.

'''

#===============================
# All code to debug is below here
#==============================
def hello(name):
    greeting = f'Hello, {name}'!'
    return greeting

def main():
  name = int(input('What is your name? '))
  if len(name < 3:
    print ('Your name is too short')
  else:
    reply = hello(name)
    print(reply)

#===============================
#All code to debug is above here
#===============================

if __name__ == '__main__':
    main()
