#Exercise 18 -- Names, Variables, Code, Functions  PTHW

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this one just take one argument
def  print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("i got nothin'.")


print_two("Talkie","Walkie")
print_two_again("Talkie","Walkie")
print_one("First!")
print_none()

#End of the exercise
