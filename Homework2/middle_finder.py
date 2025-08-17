#middle_finder.py

def middle_finder(x,y,z):
    if x < y < z or z < y < x:
        return y
    elif y < x < z or z < x < y:
        return x
    else:
        return z
print("")
for i in range(3):
    userx = int(input("Enter a number: "))
    usery = int(input("Enter a number: "))
    userz = int(input("Enter a number: "))
    print(middle_finder(userx, usery, userz), "is the middle value\n")

'''
I used a function to find the middle value using greater than and less than signs, if it was more unclear
how many values the user was going to input I likely would've used nested for loops. 
From there I used a for loop lower in the code so I could do all three tests at once to save time.
'''