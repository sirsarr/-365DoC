#Exercise 14 -- Prompting and Passing PTHW
from sys import argv

script, username, age = argv
prompt = 'Answer: '

print(f"Hi {username}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {username}?")
likes = input(prompt)

print(f"Where do you live {username} ?")
lives = input(prompt)

print("What type of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {} about liking me.
You are {} :)
You live in {}. Not sure where that is lol.
You have a {} computer. Nice.
""".format(likes, age, lives, computer))
