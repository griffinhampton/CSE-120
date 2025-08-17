#population_density.py

def population_density(population, squareMiles):
    return population / squareMiles

userMiles = int(input("How many square miles are is the city: "))
userPop = int(input("How many people live in the city: "))
print(population_density(userPop, userMiles),"people per square mile")

'''
I used an incredibly simple function to calculation population density, then I take the user inputs and plug it into the 
function. Being completely frank I probably wouldn't have used functions if it wasn't required, as
it could've been done in a print statement.
'''
