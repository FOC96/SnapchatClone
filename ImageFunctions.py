import base64
import PIL.Image as Image
from io import BytesIO
import os
import time
#from DB_Connection import Snap

def imageToText(name):
    path = os.getcwd()
    path = path+"/"+name
    print(path)
    encoded = base64.b64encode(open(path, "rb").read())
    return encoded

# def textToImage(userID):
#     snap = Snap().getConnection()
#     list = snap.getImageFile(userID)[0]
#
#     #Displays all snaps found
#     for element in list:
#         img = Image.open(BytesIO(base64.b64decode(element)))
#         Image._show(img)
#
#     #Deletes snaps showed

def showImage(encodedString):
    Image._show(Image.open(BytesIO(base64.b64decode(encodedString))))
