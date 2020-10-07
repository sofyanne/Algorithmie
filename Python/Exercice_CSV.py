#Le but est de formater les données de la chaîne de caractère dans un tableau ... de tableaux 
#possible améliorations, menu, que souhaiter vous afficher (nom, prenom...), pour aller encore plus loin on peut faire un algo de recherche.

import collections
CSV = "id,first_name,last_name,email,gender,ip_address,\
1,Briggs,Mosley,bmosley0@flavors.me,Male,117.36.35.198,\
2,Barbey,Hilbourne,bhilbourne1@webeden.co.uk,Female,88.203.109.108,\
3,Perry,Livings,plivings2@is.gd,Male,169.67.246.89,\
4,Kelci,Greggor,kgreggor3@elpais.com,Female,6.87.2.89,\
5,Shurlocke,Barby,sbarby4@nsw.gov.au,Male,34.24.154.88,\
6,Yuri,De Caroli,ydecaroli5@princeton.edu,Male,71.174.141.80,\
7,Bax,Dungate,bdungate6@devhub.com,Male,228.163.102.126,\
8,Maria,Beesey,mbeesey7@parallels.com,Female,5.147.227.184,\
9,Franny,Dallison,fdallison8@ox.ac.uk,Male,212.46.140.73,\
10,Marcellina,Vowell,mvowell9@yelp.com,Female,191.69.167.15".split(",")

row = collections.defaultdict(list)
tableau =[]

iC = 0
elt = 0


while elt < 11:
    for iR in range (0, 6, +1):
        row[elt].append(CSV[iR])
        
    tableau.append(row[elt])
    del CSV[:6]
    elt+=1
    



choix = int(input("\n\nBase de données clients:\n Vous souhaitez afficher: \n 1. Les noms.\n 2. Les prénoms.\n 3. Les emails.\n 4. Afficher la base de données complète.\n 5. Faire une recherche.\n\n"))

i=0
while (choix < 1 or choix > 5):
    print("Vous avez fait un choix invalide. Merci d'entrer un choix valide :\n")
    choix = int(input(""))

if choix == 1:
    print("Voici la liste des noms :\n")
    for i in range (0, len(tableau), +1):
        print(row[i][2])

if choix == 2:
    print("Voici la liste des prénoms :\n")
    for i in range (0, len(tableau), +1):
        print(row[i][1])

if choix == 3:
    print("Voici la liste des emails :\n")
    for i in range (0, len(tableau), +1):
        print(row[i][3])

if choix ==4:
    while i < 11:
        print(row[i])
        i+=1


#Fonction de recherche:

if choix == 5:
    recommencer = True
    while (recommencer):
        strRecherche = input("Vous pouvez effectuer une recherche uniquement à l'aide de ces éléments (id, nom, prénom, email):\n\n")
        for i in range (0, 11, +1):
            if strRecherche in row[i]:
                print(row[i])
        
        recommencer = input("\nTapez entrer pour quitter ou n'importe quelle touche pour recommencer\n")
