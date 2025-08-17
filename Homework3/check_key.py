#Griffin Hampton check key program

def check_key(key,userInput):
    if userInput in key.values():
        return True
    else:
        return False

d = {1:10,2:20,3:30,4:40,5:50,6:60}

for i in range(2):
    userInput = int(input("Enter a key value you want to check: "))

    if check_key(d,userInput):
        print("Key is present in the dictionary\n")
    else:
        print("Key is not present in the dictionary\n")

'''
My program works by using a function to check if the user input is in
the key's values, and not checking just the key. I did it this way because
if you don't clarify key.values then the if statement will only look at the
first value.
'''