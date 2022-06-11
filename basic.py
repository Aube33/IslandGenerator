import random
from PIL import ImageTk, Image

COLUMNS=50
LINES=50

textures={1:[(70,220,60),"LAND"], 0:[(60,165,220),"WATER"]}


matrice=[[random.randint(0,1) for l in range(COLUMNS)] for c in range(LINES)]
'''
matrice=[]
for c in range(LINES):
    matriceSub=[]
    for l in range(COLUMNS):
        matriceSub.append(random.randint(0,1))
    matrice.append(matriceSub)
'''
'''
for x in matrice:
    print(x)
'''   




img=Image.new(mode="RGB", size=(LINES, COLUMNS))

for w in range(img.width):
    for h in range(img.height):
        pixel=img.getpixel((w,h))
        texture=matrice[w][h]
        img.putpixel((w,h),textures[texture][0])

img.show()
