#Exercise 15 -- Reading files PTHW
#Importation du module argv pour pouvoir passer des arguments en ligne de commande
from sys import argv

#Unpacking argv
script, filename = argv

#chargement du fichier dans une variable de type file
txt = open(filename)

#Affichage du contenu
print(f"Here is your filename {filename}:")
print(txt.read())

#Repeat the process
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
