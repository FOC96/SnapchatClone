# import base64
# from DB_Connection import Snap
#
# encoded = base64.b64encode(open("/Users/fernandorc/Projects/SnapchatClone/Snap_20170528_170313.png", "rb").read())
# print(encoded)
#
# import ImageFunctions
#
# a = Snap().getConnection()
# cur = a.cursor()
#
# cur.execute("SELECT snapFile FROM snap WHERE snapID=32;")
#
# for element in cur:
#     print(str(element[0]))
#     ImageFunctions.showImage(str(element[0]))
# file = "a"
#
# #ImageFunctions.showImage(file)

from PIL import Image
from PIL import ImageFilter

img = Image.open("/Users/fernandorc/Projects/SnapchatClone/Snap_20170528_172604.png")
img = img.convert('1')
Image._show(img)


def editar1(self, img):
    imagen = Image.open(img)
    blurred = imagen.filter(ImageFilter.BLUR)

    blurred.show()
    blurred.save(img + "blurred.png")

def Grayscale(path):
    img = Image.open(path)
    img = img.convert('1')
    return img
