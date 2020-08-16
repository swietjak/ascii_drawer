from PIL import Image
import numpy as np
#import pylint
from matplotlib.image import imread


def getAverage(image):
    im = np.array(image)
    #print(type(im))
    s = im.shape
    w = s[0]
    h = s[1]
    return np.average(im.reshape(w*h))

def ReturnImage(image):
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gscale2 = "@%#*+=-:. "

    cols = 128
    scale = 0.43
    #image = Image.open("patataj.jpg").convert("L")
    W, H = image.size[0], image.size[1]
    w = W/cols
    h = w/scale
    rows = int(H/h)

    aimg = []
    for j in range(rows):
        print(j)
        y1 = int(j*h)
        y2 = int((j+1)*h)

        if j == rows - 1:
            y2 = H

        aimg.append("")

        for i in range(cols):
            #print(i)
            x1 = int(i*w)
            x2 = int((i+1)*w)

            if i == cols-1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))
            #print(img)
            avg = int(getAverage(img))

            gsval = gscale1[int((avg*69)/255)]
            aimg[j] += gsval
    return aimg
'''
f = open("out.txt", 'a')
for row in aimg:
    f.write(row + '\n')
f.close()
'''