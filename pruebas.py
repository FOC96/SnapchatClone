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
