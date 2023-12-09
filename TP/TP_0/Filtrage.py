#-*- coding: utf-8 -*-
import time
#____________Initialisation______________#
strFichierContenuFinalPoint = []
listContenuEchant = []
tabNuage=[]
tabPts=[0.0,0.0,0.0]
Fichier = 'nuage_point'
strCheminFichierPoint = Fichier +'.txt'
strCheminFichierEnregistrer = Fichier +'ReductionBruit.txt'
tabFloatPointZ = [0.0,1.1,2.2]
tabFloatPointX = [0.0,1.1,2.2]
tabNuageOUT=[]
tabBufferPts=[]
ind = 0
seuil=0.010
Temps1 = time.time()
#________________Lecture___________________#
with open(strCheminFichierPoint,'r') as FichierPoint:
    for ligne in FichierPoint:
        listNombre = ligne.split("\t")
        LongeurChaine = len(listNombre[2])
        LongeurChaine -= 2
        strNombre = listNombre[2]
        listNombre[2] = strNombre[:LongeurChaine]

        listNombre[0] = float(listNombre[0])
        listNombre[2] = float(listNombre[2])

        tabPts = listNombre
        tabNuage.append(tabPts)
#_________________Calcul____________________#
Temps2 = time.time()
for i in range (1,(len(tabNuage)-2)):


    tabFloatPointZ[0]=tabNuage[i][2]
    tabFloatPointZ[1]=tabNuage[i+1][2]
    tabFloatPointZ[2]=tabNuage[i+2][2]

    Distance1 = abs(tabFloatPointZ[2] - tabFloatPointZ[1])

    if Distance1 < seuil:
        tabNuageOUT.append(str(tabNuage[i][0])+'\t'+tabNuage[i][1]+'\t'+str(tabFloatPointZ[2])+'\n')
    else:
        ind += 1
#_______________Enregistrement________________#
Temps3 = time.time()
with open(strCheminFichierEnregistrer,'w') as File:
    File.writelines (tabNuageOUT)
    tabNuageOUT = []
    Temps4 = time.time()
    tabNuageOUT.append("Lecture : " + str(Temps2 - Temps1) + " Seconde \n Ecriture : " + str(Temps4 - Temps3) + "Seconde  \n Tous : " + str(Temps4-Temps1)+ " Seconde")
    File.writelines (tabNuageOUT)
PointRestant = i - ind
print(ind , " point supprimer sur ",i)
print("Il reste ",PointRestant,"point")
print ('Fin')

