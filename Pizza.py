import math
# Calculating how many Pizza's are needed to feed (x) amount of people

totalPeople = 0
slicesPerPerson = 0
pizzaSlices = 0

def questions():
    global totalPeople, slicesPerPerson, pizzaSlices
    totalPeople = int(input("How many people are eating? "))
    slicesPerPerson = float(input("How many slices per person? "))
    pizzaSlices = int(input("How many slices per pie? "))

def calculation():
    pizza = math.ceil((totalPeople * slicesPerPerson)/pizzaSlices) #Round off the number of pizza to feed x people
    print("You need", pizza, "pizzas to feed", totalPeople, "people.")
    leftOver = (totalPeople * slicesPerPerson) - (pizzaSlices * pizza)
    print("There will be", abs(leftOver), "leftover slices.")

def main():
    questions()
    calculation()

main()