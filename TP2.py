"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  12
Noms et matricules : Mohamed Kaydon  (2273422), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv


csvfile = open('/Users/kaydon/Desktop/INF1007/2024A-TP02-Enonce/collection_bibliotheque.csv', newline='')
bibliothèque={}

c = csv.DictReader(csvfile)



#print(f' \n Bibliotheque initiale : {bibliothèque} \n')

for row in c:
    L=[]
    L.append(row['auteur'])
    L.append(row["titre"])
    L.append(row["date_publication"])
    bibliothèque[row["cote_rangement"]]= L
    






print(f' \n Bibliotheque initial, E1 \n')
for q, w in bibliothèque.items():

    print(f"{q} = {w}")


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
cc = open('/Users/kaydon/Desktop/INF1007/2024A-TP02-Enonce/nouvelle_collection.csv', newline='')
a= csv.DictReader(cc)
for mop in a:
    if mop["cote_rangement"] not in bibliothèque:
        l=[]
        l.append(row['auteur'])
        l.append(row["titre"])
        l.append(row["date_publication"])
        bibliothèque[mop["cote_rangement"]]=l
        print(f"Le livre {mop['cote_rangement']} {mop['titre']} par {mop['auteur']} a été ajouté avec succès")
    else:
        print(f"Le livre {mop['cote_rangement']} {mop['titre']} par {mop['auteur']} est déjà dans la collection")





    






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
biblio =bibliothèque.copy() 
for i,value in bibliothèque.items():
    if 'William Shakespeare' in value:
        biblio["W"+i]=bibliothèque[i]
        del biblio[i]




        
    

















########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

s = open('/Users/kaydon/Desktop/INF1007/2024A-TP02-Enonce/emprunts.csv', newline='')


a = csv.DictReader(s)
emprunt={}
for pew in a:
        li=[]
        li.append(pew['date_emprunt'])
        emprunt[pew["cote_rangement"]]=li 

for x in biblio.keys():
    e={}
    
    if x in emprunt:
        e["emprunt"]="emprunté"
        e["date_emprunt"]=emprunt[x][0]
        biblio[x].append(e)
    else:
        e["emprunt"]="disponible"
    
        biblio[x].append(e)











########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

import datetime 
from datetime import date 



date_today= datetime.date.today()




for m in emprunt.keys(): 
        
        d=emprunt[m][0].split("-")
        annee,mois,jour= int(d[0]),int(d[1]),int(d[2]) 
        diff= (date(date_today.year,date_today.month, date_today.day)-date(annee,mois,jour)).days
        if 'emprunté' == biblio[m][3]["emprunt"]:
            if 365 > diff > 30: 
                frais=  2*(diff-30)
                biblio[m][3]["frais_de_retard"]=frais
                if frais > 100 :
                    frais= 100 
                    biblio[m][3]["frais_de_retard"]=frais
                    
            
            elif diff > 365 :
                frais=100 
                biblio[m][3]["frais_de_retard"]=frais
                biblio[m][3]["Livre_perdu"]="perdu"
                
         

        
      
        

    






print(f' \n Bibliotheque avec ajout des retards et frais, avec ajout des emprunts et modification des cotes :E5,E4,E3  \n')
for key, value in biblio.items():

    print(f"{key} = {value}")
for q in emprunt.keys():
    if len(biblio[q]) >= 4:
        if "Livre_perdu" in biblio[q][3]:
         print(biblio[q][1], "est un livre perdue , E5")




