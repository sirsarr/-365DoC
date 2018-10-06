#Exercise 8, Printing Printing

formatter= "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format('one','two','three','four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter, formatter, formatter))


# This is the Butterfy Effect
print(formatter.format(
    "Heating up, baby I'm just heating up\n",
    "Need ya love not a need it'a a must\n",
    "Feelin' stuck, you know how to keep me up\n",
    "Icy love, icy like a hockey puck\n"
))
