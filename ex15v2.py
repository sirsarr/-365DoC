#Exercise 15 Version 2 -- Reading files PTHW
#Passage du nom du fichier par l'utilisateur.

#Prompting
print("Salut, veuillez entrer le nom du fichier que vous voulez ouvrir.")

#Getting the file's name
filename = input("> ")

#Opening the file
content = open(filename)

#Affichage du contenu du fichier
print(content.read())


#Much shorter than v1 haa!
