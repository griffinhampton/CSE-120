# Griffin Hampton CSE 120 Lab-3

numbers = []

for i in range(13):
    x = int(input("Enter a number: "))
    numbers.append(x)

y = int(input("Enter how much you want to multiply your list by: "))
for number in range(len(numbers)):
    z = (numbers[number])*y
    numbers[number]=z

print(numbers)

'''
1:
The advantage of using a loop for the list is that I can control exactly how 
big the array will be.
2:
I used a for loop because it is less work than a while loop, albeit marginally less work.
It automatically moved on the loop instead of me having to move it ahead myself.
Also the ability to get a particular number in the range using len is very useful, and it's easier to do in for loops
3:
I worked by myself
'''

