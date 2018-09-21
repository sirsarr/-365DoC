#Exercise 19 -- Functions and Variables

#Function definition, it takes two args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

#Giving directly two numbers to the function as args
print("We can just give the function numbers directly:")
cheese_and_crackers (20,30)

#setting
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#using variables as args for to run the function
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


#Doing math ;)
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

#Getting input fro the user and using them as args for our defined function
print("Calling the function...")
cheese_and_crackers(input("How many cheeses do you have?\n>"),input("How many boxes of crackers do you have?\n>"))

#End Of this exercise
