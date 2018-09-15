#Exercice 4 - Learn Python The Hard Way

#Affectations de valeurs à des variables + quelques calculs élémentaires
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity =  cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


#Affichage de la valeur de ses variables dans des phrases.
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")


#Un petit calcul avec des variables pour terminer
i = 65
j = 9
x = round(i / j)
y=i%j
print("Pour le petit calcul",i,"%",j," = ",y)
print("car",i,"/",j,"=",x,"et",j,"*",x,"=",x*j)
print("Je n'ai pas menti lol, il reste bien",i-x*j)

##End
