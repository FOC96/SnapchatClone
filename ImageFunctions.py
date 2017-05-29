import base64
import PIL.Image as Image
from PIL import ImageFilter
from io import BytesIO
import os
import time
from DB_Connection import Snap
import localFiles

def imageToText(name):
    path = os.getcwd()
    path = path+"/"+name
    print(path)
    encoded = base64.b64encode(open(path, "rb").read())
    return encoded

def textToImage():
    snap = Snap().getConnection()
    userID = localFiles.getLocalUserInfo()[0]
    list = snap.getImageFile(userID)[0]

    #Displays all snaps found
    for element in list:
        img = Image.open(BytesIO(base64.b64decode(element)))
        Image._show(img)

    #Deletes snaps showed

def showImage(encodedString):
    #Image._show(Image.open(BytesIO(base64.b64decode(encodedString))))
    Image._show(Image.open(base64.b64decode(encodedString)))

def showImg(name):
    path = os.getcwd()
    path = path+"/"+name
    img = Image.open(path)
    img.show()

# EFECTOS
from PIL import Image, ImageFilter, ImageOps


def editar1(img):#Blurred
    imagen = Image.open(img).filter(ImageFilter.GaussianBlur(radius=15))
    imagen.convert("RGB")
    imagen.save(img)

def make_linear_ramp(white):
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r * i / 255, g * i / 255, b * i / 255))
    return ramp

def editar2(img):#Sepia
    sepia = make_linear_ramp((255, 240, 192))
    im = Image.open(img)
    im = im.convert('L')
    im.putpalette(sepia)
    im = im.convert('RGB')

    im.save(img)

def editar3(img):#GrayScale
    imagen = Image.open(img).convert('LA')
    imagen.save(img)
