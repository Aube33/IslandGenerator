import random
from PIL import Image

COLUMNS=256
LINES=256
ECART_C=COLUMNS//9
ECART_L=LINES//9

#random.seed(1) #OPTIONAL /!\

textures={0:[(60,165,220),"SEA_WATER"], 0.5:[(235,235,50),"SAND"], 1:[(70,220,60),"LAND"]}

#===== Default Generation =====
#= Sea Generation =
matrice=[[0 for lines in range(COLUMNS)] for columns in range(LINES)]
'''
====================
====================
====================
====================
====================
====================
====================
'''

#= Island Square Default Generation =
for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        matrice[c][l]=1
'''
====================
====############====
====############====
====############====
====############====
====############====
====================
'''
#==========


#===== Terraforming of square =====

#=== Global Erosion ===
erosionGenMin=0.41
erosionGenMax=0.49

#Left to Right, Top to Down
for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        texture=matrice[c][l]
        if texture==1 and (matrice[c+1][l]==0 or matrice[c-1][l]==0 or matrice[c][l+1]==0 or matrice[c][l-1]==0):
            if random.random()<=random.uniform(erosionGenMin, erosionGenMax):
                matrice[c][l]=0
                if random.random()<=0.5:
                    matrice[c+1][l]=0
                if random.random()<=0.5:
                    matrice[c-1][l]=0
                if random.random()<=0.5:
                    matrice[c][l+1]=0
                if random.random()<=0.5:
                    matrice[c][l-1]=0
            else:
                matrice[c][l]=1  

#Left to Right, Down to Top
for c in range(ECART_C, len(matrice)-ECART_C):
    for l in reversed(range(ECART_L, len(matrice[c])-ECART_L)):        
        texture=matrice[c][l]
        if texture==1 and (matrice[c+1][l]==0 or matrice[c-1][l]==0 or matrice[c][l+1]==0 or matrice[c][l-1]==0):
            if random.random()<=random.uniform(erosionGenMin, erosionGenMax):
                matrice[c][l]=0
                if random.random()<=0.5:
                    matrice[c+1][l]=0
                if random.random()<=0.5:
                    matrice[c-1][l]=0
                if random.random()<=0.5:
                    matrice[c][l+1]=0
                if random.random()<=0.5:
                    matrice[c][l-1]=0
            else:
                matrice[c][l]=1  

#Right to Left, Bottom to Top
for c in reversed(range(ECART_C, len(matrice)-ECART_C)):
    for l in reversed(range(ECART_L, len(matrice[c])-ECART_L)):        
        texture=matrice[c][l]
        if texture==1 and (matrice[c+1][l]==0 or matrice[c-1][l]==0 or matrice[c][l+1]==0 or matrice[c][l-1]==0):
            if random.random()<=random.uniform(erosionGenMin, erosionGenMax):
                matrice[c][l]=0
                if random.random()<=0.5:
                    matrice[c+1][l]=0
                if random.random()<=0.5:
                    matrice[c-1][l]=0
                if random.random()<=0.5:
                    matrice[c][l+1]=0
                if random.random()<=0.5:
                    matrice[c][l-1]=0
            else:
                matrice[c][l]=1

#Right to Left, Top to Bottom
for c in reversed(range(ECART_C, len(matrice)-ECART_C)):
    for l in range(ECART_L, len(matrice[c])-ECART_L):        
        texture=matrice[c][l]
        if texture==1 and (matrice[c+1][l]==0 or matrice[c-1][l]==0 or matrice[c][l+1]==0 or matrice[c][l-1]==0):
            if random.random()<=random.uniform(erosionGenMin, erosionGenMax):
                matrice[c][l]=0
                if random.random()<=0.5:
                    matrice[c+1][l]=0
                if random.random()<=0.5:
                    matrice[c-1][l]=0
                if random.random()<=0.5:
                    matrice[c][l+1]=0
                if random.random()<=0.5:
                    matrice[c][l-1]=0
            else:
                matrice[c][l]=1  
#======

#=== Corrections ===
#= Remove Littles Islands =
for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        if matrice[c][l]==1:
            counterDirections={
            "r":1, # 🡒
            "l":1, # 🡐
            "t":1, # 🡑
            "b":1, # 🡓

            "tr":1, # ↗
            "tl":1, # ↖
            "br":1, # ↘
            "bl":1, # ↙
            }

            counter=1 #Size of the little island
            MaxIslandCounterSize=5 #Max: 36

            coorToCorrect=[[c, l]]
            counterDirections_valuesOK=len(counterDirections)

            IslandMaxDensity=2

            while(counter<=MaxIslandCounterSize and counterDirections_valuesOK>=IslandMaxDensity):
                #= Check the density of littles islands =
                counterDirections_valuesOK=0
                for v in counterDirections.values():
                    if v==1:
                        counterDirections_valuesOK+=1

                #=== Detections ===
                if not(matrice[c+counter][l]==1) and counterDirections["r"]==1:
                    counterDirections["r"]=0
                    coorToCorrect.append([c+counter, l])

                if not(matrice[c-counter][l]==1)  and counterDirections["l"]==1:
                    counterDirections["l"]=0
                    coorToCorrect.append([c-counter, l])

                if not(matrice[c][l+counter]==1)  and counterDirections["t"]==1:
                    counterDirections["t"]=0
                    coorToCorrect.append([c, l+counter])

                if not(matrice[c][l-counter]==1)  and counterDirections["b"]==1:
                    counterDirections["b"]=0
                    coorToCorrect.append([c, l-counter])


                if not(matrice[c+counter][l+counter]==1)  and counterDirections["tr"]==1:
                    counterDirections["tr"]=0
                    coorToCorrect.append([c+counter, l+counter])
                    
                if not(matrice[c-counter][l-counter]==1)  and counterDirections["bl"]==1:
                    counterDirections["bl"]=0
                    coorToCorrect.append([c-counter, l-counter])

                if not(matrice[c-counter][l+counter]==1)  and counterDirections["tl"]==1:
                    counterDirections["tl"]=0
                    coorToCorrect.append([c-counter, l+counter])

                if not(matrice[c+counter][l-counter]==1)  and counterDirections["br"]==1:
                    counterDirections["br"]=0
                    coorToCorrect.append([c+counter, l-counter])

                counter+=1
                #======

            #= Apply detected corrections =
            if(counter<=MaxIslandCounterSize):
                for x in coorToCorrect:
                    matrice[x[0]][x[1]]=0

#= Remove One Pixels Islands =
for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        if matrice[c][l]==1 and matrice[c+1][l]==0 and matrice[c-1][l]==0 and matrice[c][l+1]==0 and matrice[c][l-1]==0:
            matrice[c][l]=0
#======

#=== Add Sand ===
for c in range(ECART_C, len(matrice)-ECART_C):
    for l in range(ECART_L, len(matrice[c])-ECART_L):
        if matrice[c][l]==1:
            if matrice[c+1][l]==0:
                matrice[c+1][l]=0.5

            if matrice[c-1][l]==0:
                matrice[c-1][l]=0.5

            if matrice[c][l+1]==0:
                matrice[c][l+1]=0.5

            if matrice[c][l-1]==0:
                matrice[c][l-1]=0.5     
            

            if matrice[c+1][l+1]==0 and random.random()<=0.3:
                matrice[c+1][l+1]=0.5  

            if matrice[c-1][l-1]==0 and random.random()<=0.3:
                matrice[c-1][l-1]=0.5 

            if matrice[c-1][l+1]==0 and random.random()<=0.3:
                matrice[c-1][l+1]=0.5 

            if matrice[c+1][l-1]==0 and random.random()<=0.3:
                matrice[c+1][l-1]=0.5   
#======

#==========


#===== Show Island Image =====
island=Image.new(mode="RGB", size=(LINES, COLUMNS))
for w in range(island.width):
    for h in range(island.height):
        pixel=island.getpixel((w,h))
        texture=matrice[w][h]
        island.putpixel((w,h),textures[texture][0])

island.show()
#==========
