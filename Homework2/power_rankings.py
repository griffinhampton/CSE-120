#power_rankings.py

acc_womens_basketball = ["Notre Dame", "Duke", "Virginia Tech", "Louisville", "Florida State",
"Miami", "North Carolina", "NC State", "Syracuse", "Clemson", "Boston College", "Wake Forest",
"Virginia", "Georgia Tech", "Pitt"]

userSchool = input("Please enter a school name:")
print("Schools better than", userSchool, ":\n")
i = 0
for i in range(len(acc_womens_basketball)):
    if acc_womens_basketball[i] == userSchool:
        i+=1
        break

    print(acc_womens_basketball[i])

print("Schools worse than", userSchool, ":\n")

for j in range(len(acc_womens_basketball)-i):
    print(acc_womens_basketball[j+i])


'''
OK SO this code is a bit of a jumble because I came up with a sorta dumb way to do the assignment
I decided that instead of using the colon in the array to determine if something was before or after
I just used a for loop to go through the array and check if the current school was equal to the user input
if it was, then I break out of the loop and move on to the next school.
From there I added 1 to i so the program wouldn't print the current school and did it all like that.
'''
