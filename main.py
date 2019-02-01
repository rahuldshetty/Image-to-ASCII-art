from PIL import Image
import numpy as np

asciis=(list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"))
sz=len(asciis)



def conv2ascii(img,resizeFactor=0.1):
	img=img.resize((int(img.size[0]*resizeFactor),int(img.size[1]*resizeFactor)),Image.BILINEAR)
	w,h=img.size
	s=""
	for j in range(h):
		for i in range(w):
			lum=255-img.getpixel((i,j))
			s+= asciis[lum//sz]
		s+="\n"
	return s

f='sample.jpg'
img=Image.open(f).convert('L')
s=conv2ascii(img)
open('result.txt','w').write(s)


