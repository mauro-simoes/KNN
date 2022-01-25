import csv
import matplotlib.pyplot as plt
from math import sqrt


def convert(dico): 
    '''In: dico le dictionnaire
    Out: le dictionnaire en français'''
    return {'longueur_petale':float(dico['petal_length']),'largeur_petale':float(dico['petal_width']),'espece': dico['species']}

#on ouvre le fichier qui contient les données des types d'iris
fichier=open("iris_data_set.csv") 
table=list(csv.DictReader(fichier,delimiter=",")) 
iris = [convert(ligne) for ligne in table]
fichier.close()

with open("NouveauFichier.csv","w") as sortie:     
    objet=csv.DictWriter(sortie,['longueur_petale','largeur_petale','espece'])
    objet.writeheader()
    objet.writerows(iris)


def d(xa,ya,xb,yb):
    '''In: xa,ya,xb,yb les coordonnées de deux points
    Out: la distance entre les deux points'''
    return sqrt((xb-xa)**2+(yb-ya)**2)

def knn(liste_dico,k,longueur,largeur):
    '''In: liste de dictionnaires, k longueur et largeur de l'iris
    Out: liste des k plus proches voisins'''
    L=[]
    xb=longueur
    yb=largeur
    for x in liste_dico:
        xa=x['longueur_petale']
        ya=x['largeur_petale']
        espece=x['espece']
        distance=d(xa,ya,xb,yb)
        L.append((distance,espece))
    L=sorted(L,key=lambda x: x[0])
    return L[0:k] 

def decision(liste_dico,k,longueur,largeur):
    '''In: liste de dictionnaires, le parametre k et la longueur et largeur de l'iris à tester 
    Out: l'espece attribuée'''
    L=knn(liste_dico,k,longueur,largeur)
    s=0
    versi=0
    virgi=0
    for x in L:
        if x[1]=='setosa':
            s+=1
        elif x[1]=='virginica':
            virgi+=1
        else:
            versi+=1
    if s>versi and s>virgi:
        return 'setosa'
    elif versi>s and versi>virgi:
        return 'versicolor'
    elif virgi>s and virgi>versi:
        return 'virginica'


longueur,largeur,k =input("Entrez la longueur(<8) puis la largeur(<3) de la plante ainsi que le nombre de voisins: ").split()
float(longueur)
float(largeur)
int(k)


fichier=open("NouveauFichier.csv") 
table=list(csv.DictReader(fichier,delimiter=",")) 
X_iris_0=[float(ligne['longueur_petale']) for ligne in table if ligne['espece']=='setosa'] 
Y_iris_0=[float(ligne['largeur_petale']) for ligne in table if ligne['espece']=='setosa'] 
X_iris_1=[float(ligne['longueur_petale']) for ligne in table if ligne['espece']=='versicolor']
Y_iris_1=[float(ligne['largeur_petale']) for ligne in table if ligne['espece']=='versicolor'] 
X_iris_2=[float(ligne['longueur_petale']) for ligne in table if ligne['espece']=='virginica'] 
Y_iris_2=[float(ligne['largeur_petale']) for ligne in table if ligne['espece']=='virginica'] 
fichier.close() 
fig=plt.figure() 
plt.scatter(X_iris_0, Y_iris_0, color='g', label='setosa',s = 20, marker = '*') 
plt.scatter(X_iris_1, Y_iris_1, color='r', label='versicolor',s = 20, marker = '.') 
plt.scatter(X_iris_2, Y_iris_2, color='b', label='virginica',s = 20, marker = '+') 
plt.scatter(float(longueur),float(largeur), color='orange', label='Iris', s=30, marker='v')
plt.legend()
plt.xlabel('Longueur des pétales') 
plt.ylabel('Largeur des pétales') 
Liste= knn(iris,int(k),float(longueur),float(largeur))
rad=Liste[int(k)-1][0]
cercle = plt.Circle((float(longueur),float(largeur)),radius=(rad), color='green', fill=False)
ax=plt.gca()
ax.add_patch(cercle)
plt.axis('scaled')
fig.savefig('plot.png')

print(decision(iris,int(k),float(longueur),float(largeur)))
