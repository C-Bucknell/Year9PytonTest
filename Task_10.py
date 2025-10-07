#Task 10 Week Days
'''
Task 10 Week Days (10 marks)

Write a function called format_days which takes a list of strings in its argument.

Each string is the short form for a day, for example: ‘Mon', 'Tue', 'Wed', etc.

format_days should return a new list, with each day converted to it's full 
name: 'Monday', 'Tuesday', 'Wednesday', etc.

For example, when we run:
-------------------------
result = format_days(['Mon', 'Wed','Fri'])
print(result)
-------------------------
then we expect the output to be:
-------------------------
['Monday','Wednesday','Friday']
-------------------------

If there is a short day name that is not recognised, you should ignore this day and 
filter it from the formatted list.

For example, if we invoked your function like:
-------------------------
result = format_days(['Sat','Fun', 'Tue','Thu'])
print(result)
-------------------------
then we expect the output to be:
-------------------------
['Saturday','Tuesday','Thursday']
-------------------------

Here is a table showing the short and long forms for the recognised days of the week.

Short Name | Full Name
===========|==========
Mon	       | Monday
Tue	       | Tuesday
Wed	       | Wednesday
Thu	       | Thursday
Fri	       | Friday
Sat	       | Saturday
Sun	       | Sunday

Note: You will need to code more that just the function. 
The main part of your program should include the test above. 

HINT: A dictionary works well for this function.

'''

 #===============================
 # Write your code below here
 #==============================

def format_days(short_days):
    # Dictionary mapping short day names to full day names
    day_mapping = {
        'Mon': 'Monday',
        'Tue': 'Tuesday',
        'Wed': 'Wednesday',
        'Thu': 'Thursday',
        'Fri': 'Friday',
        'Sat': 'Saturday',
        'Sun': 'Sunday'
    }
    
    # List to hold the full day names
    full_days = []
    
    # Iterate through the input list and convert to full names
    short_days_list= short_days.split(',')
    for day in short_days_list:
        if day.strip() in day_mapping:
            full_days.append(day_mapping[day.strip()])
    
    return full_days

#===============================
# End of your code here
#===============================

def main():
   short_days_list = input("Enter short day names separated by commas: ")
   full_days = format_days(short_days_list)
   print(full_days)
    


if __name__ == '__main__':
    main()
