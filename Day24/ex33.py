#Exercise 33 - While loops

#this function returns a list with all the numbers in the 0 - nbr
def whileloop(nbr, incr):
    i = 0
    numbers = []
    while i < nbr :
        print(f"At the top i is {i}")
        numbers.append(i)

        i += incr

        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")


    return numbers



#Number input from the user, conversion in integer
x = (int)(input('Enter a number: '))
y = (int)(input('Enter the incrementation value: '))

#function call
nbrlist = whileloop(x,y)

#printing the result
for num in nbrlist:
    print(num)
