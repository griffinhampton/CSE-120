#Griffin Hampton CSE-120
import random
from random import choice


class Parent:
    def __init__(self, gene1,gene2):
        self.gene1 = gene1
        self.gene2 = gene2

class Child:
    def __init__(self, parent1,parent2):
        self.parent1 = parent1
        self.parent2 = parent2
        self.gene1 = random.choice([parent1.gene1,parent1.gene1])
        self.gene2 = random.choice([parent2.gene2,parent2.gene2])

    def findEyeColor(self,gene1,gene2):
        if self.gene1 == "blue" and self.gene2 == "blue":
            return "blue"
        else:
            return "brown"
done = False
while not done:
    p1g1,p1g2 = input("Enter the first parent's eye color genes (seperated by space): ").split()
    p2g1,p2g2 = input("Enter the second parent's eye color genes (seperated by space): ").split()

    p1 = Parent(p1g1,p1g2)
    p2 = Parent(p2g1,p2g2)
    child = Child(p1,p2)
    print(f"Child's genes: {child.gene1} {child.gene2}")
    print(f"Child's eye color: {child.findEyeColor(p1g1,p1g2)}")

    userPlay = input("Press enter to continue or type 'done' to quit: ")
    if userPlay == 'done':
        done = True
        break

'''
1: The hardest part of using objects is knowing when certain variables are redundant or unnecessary.
And also using functions within classes.
2: It allows for more flexibility and reusability, in this particular program it allowed for the child to 
easily take the randomized parent genes.
3: I worked alone
'''