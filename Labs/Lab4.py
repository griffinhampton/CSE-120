#Griffin Hampton CSE-120 Lab 4

car_dict = {}

done = False
while not done:
    make = input("Enter the make of your car (type done to quit): ")
    if make == 'done':
        break
    model = input("Enter the model of your car: ")

    car_dict[model] = make

while not done:
    query_model = input("Enter a model to search for: ")

    car_make = car_dict.get(query_model)

    if car_make == None:
        print("Sorry, we don't have a", query_model)
    else:
        print("The make of", query_model, "is", car_make)

    finished=input("Press enter to search again or type 'done' to quit: ")
    if finished == 'done':
        done = True

'''
1: Dictionaries work so well for problems like this because they appear more structured than a normal array,
and allow for more data to be stored more effectively. And because there aren't many values in this dictionary you can
access everything with just one .get, and that's sick.

2: I worked by myself, but used your video for a lot of inspiration.
'''