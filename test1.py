import random
from PIL import ImageTk, Image
import time

COLUMNS=512
LINES=512
ECART_C=COLUMNS//9
ECART_L=LINES//9

#random.seed(10)

textures={0:[(60,165,220),"SEA_WATER"], 0.01:[(98,183,227),"FRESH_WATER"], 0.5:[(235,235,50),"SAND"], 1:[(70,220,60),"LAND"]}

matrice=[[0 for l in range(COLUMNS)] for c in range(LINES)]
for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        matrice[c][l]=1

for c in range(ECART_C,len(matrice)-ECART_C):
    for l in range(ECART_L,len(matrice[c])-ECART_L):
        #texture=random.choice([1])
        texture=matrice[c][l]
        
        if round(matrice[c+1][l], 1)==0.0 or round(matrice[c-1][l], 1)==0.0 or round(matrice[c][l+1], 1)==0.0 or round(matrice[c][l-1], 1)==0.0:
            if random.random()<0.15:
                texture=0.01
            else:
                texture=1
        if texture==1:
            if round(matrice[c+1][l], 1)==0.0:
                matrice[c+1][l]=0.5
            if round(matrice[c-1][l], 1)==0.0:
                matrice[c-1][l]=0.5
            if round(matrice[c][l+1], 1)==0.0:
                matrice[c][l+1]=0.5
            if round(matrice[c][l-1], 1)==0.0:
                 matrice[c][l-1]=0.5
        
        else:
            matrice[c][l]=0.01
            matrice[c+1][l]=0.01
            matrice[c-1][l]=0.01
            #Blem en dessous
            matrice[c][l+1]=0.01
            matrice[c][l-1]=0.01
            

for x in matrice:
    print(x)   
    
    
island=Image.new(mode="RGB", size=(LINES, COLUMNS))
for w in range(island.width):
    for h in range(island.height):
        pixel=island.getpixel((w,h))
        texture=matrice[w][h]
        island.putpixel((w,h),textures[texture][0])

island.show()
