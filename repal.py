import os, json
from PIL import Image

in_path = "input/"

input_list = []

for file in os.listdir(in_path):
        if file.endswith(".png"):
            input_list.append(Image.open(in_path+str(file)))

palette_path = "palettes/"

palette_list = []

for file in os.listdir(palette_path):
    if file.endswith(".png"):
        palette_list.append(Image.open(palette_path+str(file)))

maxval = 256

def remap_palette(inimg,palette):
    inimg = inimg.convert("RGB")
    inpix = inimg.load()
    palpix = palette.load()
    outimg = Image.new("RGB",inimg.size,"black")
    outpix = outimg.load()
    for i in range(inimg.size[0]):
        for j in range(inimg.size[1]):
            val = inpix[i,j][0] + inpix[i,j][1] + inpix[i,j][2]
            val /= 3
            mval = maxval - val
            mval *= palette.size[0]
            mval /= maxval
            pos = mval-1
            try:
                outpix[i,j] = palpix[pos,0]
            except Exception:
                print "{} {} {}".format(mval, pos,palette.size[0])
    return outimg

for i, inimg in enumerate(input_list):
    for n, palimg in enumerate(palette_list):
        outimg = remap_palette(inimg,palimg)
        outimg.save("output/"+str(i)+'_'+str(n)+".png")


