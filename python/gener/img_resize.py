from PIL import Image
import os
 
# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
imgPath = './corel1k/'
thumbnailsPath = './thumbnails/'
imlist = [os.path.join(imgPath,f) for f in os.listdir(imgPath) if f.endswith('.jpg')]

# adjust width and height to your needs
(width,height)= (400,400)
ext = ".jpg" 
 
for index,imName in enumerate(imlist):
    im = Image.open(imName)
	# use one of these filter options to resize the image
    resized_im = im.resize((width, height), Image.NEAREST)       # use nearest neighbour
	#resized_im = im.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
	#resized_im = im.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
	#resized_im = im.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
    outImgName = thumbnailsPath+os.path.basename(imName)[:-4]+ext
    resized_im.save(outImgName)
    print ("save %s image finised" %(os.path.basename(imName)[:-4]+ext))
