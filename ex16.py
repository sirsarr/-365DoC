#Exercise 16 -- Reading and Writting Files

#Importation de argv
from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#Attente pour poursuivre ou pas
input('?')

#ouverture du fichier
target = open(filename, 'w')

#Truncating
print("Truncating the file. Goodbye!")
target.truncate()

#Receuil des phrases à écrire
print("Now I'm going to ask you fo three lines.")
line1 = input("line 1: ")
line2 = input("line2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file {}".format(filename))

#Ecriture de ces phrases dans le fichier
target.write(line1+'\n'+line2+'\n'+line3+'\n')

#Fermeture du fichier
print("We closed the file.")
target.close()

#Lecture du fichier
print("""
Do you want to read the file?
Hit CTRL-C(^C) if you don't.
Hit ENTER if you do want that.""")

input('?')

#Ouverture et affichage du fichier
print("We're going to open and read the file {}".format(filename))
target = open(filename)

print("Here's the content of the file:")
print(target.read())

#Fermeture du fichier
target.close()
print("And finally, the file had been closed.")
