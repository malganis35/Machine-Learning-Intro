# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 17:55:29 2017

@author: caotrido
"""

#%% Les variables en Python

# Assigner des variables
a = b = 1
print "Mon nombre est égale à", a

# Les lists
c = [1, 2, 3]
d = ["nono", "cao", "toto"]
print c
print d

# Les dictionnaires (structure de matlab)
dict = {}
dict["key"] = "id_451"
dict["value"] = {}
dict["value"][0] = "19 ans"
dict["value"][1] = "Rennes"
print dict

# Les arrays (matrice de matlab)
import numpy as np
e = np.array(c)
print e

# Les dataframe (table de matlab)
import pandas as pd
df = pd.DataFrame(data = e, columns = {"name"})
print df


#%% Les opérations élémentaires
# Créer une conditionnelle. 
# Note: en Python, il n'y a pas de end. Faire attention à l'indentation
# Les différents signe : ==, !=, >=, >, etc.
if a > 0:
    print "Je suis un nombre positif"
elif a == 0:
    print "Je suis un nombre nulle"
else:
    print "Je suis un nombre négatif"
 
# La boucle for
# En Python, la boucle for n'a pas de end.
for i in range(0,5):
    print "- Valeur du nombre actuelle:", i
    
# La boucle for peut aussi s'effectuer sur une liste
my_list = [1,2,3,4,5]
for l in my_list:
    print "-Valeur actuelle de la liste:", l

# La boucle While
bool = False
counter = 0
while bool == False:
    print "- Actual counter:", counter
    if counter < 4:
        counter = counter + 1
    else:
        bool = True

#%% Créer une fonction en python
        
def compute_2_numbers(num1, num2):
    '''
    INPUT: num1 et num2 sont 2 chiffres
    OUTPUT: retourne la somme, la différence et la multiplication des 2 nombres
    '''
    sum         = num1 + num2
    diff        = num1 - num2
    multiply    = num1 * num2
    return sum, diff, multiply

# define the number
g = 1
h = 2
# Execute function
i, j, k = compute_2_numbers(g, h)

# print
print "the sum is equal to", i
print "the difference is equal to", j
print "the multiplication is equal to", k


#%% Les packages.
# Les packages en python représente les modules que l'on va ajouter pour 
# faire fonctionner notre code (ce sont les fonctions externes)

import numpy as np
import pandas as pd


#%% Créer un package et l'importer
# Pour te permettre de créer des templates de package que tu peux te créer pour toi,

import mypackage as MP
new_number = MP.my_fct1(3)