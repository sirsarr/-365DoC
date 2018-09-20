#Exercise 16 -- More Files

from sys import argv #module argv pour pouvoir prendre les arguments depuis la ligne de commande
from os.path import exists #module exists pour check si un fichier existe

#Unpacking variables
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

#Verification de l'existence du fichier de destination.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#Ouverture du fichier source et écriture du contenu du fichier source dans le fichier de destination
out_file =open(to_file,'w')
out_file.write(indata)

print("Alright, all done!")

#Fermeture des fichiers
in_file.close()
out_file.close()
