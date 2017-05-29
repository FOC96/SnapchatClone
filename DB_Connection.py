# DB connection
import pymysql
# To get the device's IP address
import socket
# Password encryption
from passlib.hash import pbkdf2_sha256
# Snap's datetime
import time
#To get the device's MAC address
from uuid import getnode
import localFiles
import ImageFunctions

class SnapDB:
    # Get conection with database -> connection
    def getConnection(self):
        # Database Variables
        db_host = 'localhost'
        db_port = 3306
        db_user = 'root'
        db_password = ''
        db_charset = 'utf8'
        db_database = 'snapchat'

        conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_password, db=db_database, charset=db_charset)
        return conn


    # Gets the device's IP Address --> ipAddress
    def getIPadress(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('192.0.0.8', 1027))
        ipAddress = s.getsockname()[0]
        return ipAddress


    # Adds a new user to the database
    def addUser(self, nickName, name, password):
        # Getting connection
        conn = self.getConnection()
        cur = conn.cursor()

        # Password encrypted
        password = pbkdf2_sha256.hash(password)

        # INSERT command
        cur.execute("INSERT INTO user(userNickname, userName, userPassword, userIPAddress) VALUES('"+nickName+"', '"+name+"', '"+password+"', '"+self.getIPadress()+"');")

        # Changes are saved through 'commit()'
        conn.commit()

        # Closing cursor and connection
        cur.close()
        conn.close()


    # Checks if the userNickname and Password are correct --> userID/void
    def checkLogin(self, nickname, password):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM user;")

        session = False
        name = ""
        userID = 0

        for element in cur:
            # Verifies the given password and the encrypted one
            check = pbkdf2_sha256.verify(password, element[3])

            if check == True and element[1] == nickname:
                session = True
                name = element[2]
                userID = element[0]
                break
        cur.close()
        conn.close()

        if session == True:
            a = SnapDB()
            localFiles.saveUserInfoLocally(a.getUserData(userID)[0], a.getUserData(userID)[1], a.getUserData(userID)[2], a.getUserData(userID)[3])
            print("Sesión iniciada con éxito,", name)
            self.updateIP(userID)
            return True, userID
        else:
            print("Error en los campos")
            return False, None


    def getUserData(self, userID):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("SELECT userID, userNickname, userName, userIPAddress FROM user WHERE userID = "+str(userID))

        for element in cur:
            userID = element[0]
            userNickname = element[1]
            userName = element[2]
            userIPaddress = element[3]

        cur.close()
        conn.close()

        return userID, userNickname, userName, userIPaddress

    # Updates the user's IP Address in the DB
    def updateIP(self, userID):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("UPDATE user SET userIPAddress = '"+self.getIPadress()+"' WHERE userID = "+str(userID)+"")
        conn.commit()
        cur.close()
        conn.close()


class Snap(SnapDB):
    def saveSnap(self, snapName, snapSender, snapReceiver, snapFile):
        conn = SnapDB()
        conn = conn.getConnection()
        cur = conn.cursor()
        cur.execute("INSERT INTO snap(snapName, snapSender, snapReceiver, snapStatus, snapFile) VALUES(\'"+str(snapName)+"\', "+str(snapSender)+", "+str(snapReceiver)+", 0, 'here goes the base64 encoded string from the image');")
        conn.commit()
        cur.close()
        conn.close()

    def getImageFile(self, snapReceiver):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("SELECT snapID, snapFile FROM snap WHERE snapReceiver = "+str(snapReceiver)+";")

        deleteIDs = []
        snapsReceived = []

        for result in cur:
            deleteIDs.append(result[0])
            snapsReceived.append(result[1])

        return snapsReceived, deleteIDs

    def getImageName(self, snapReceiver):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("SELECT snapID, snapName FROM snap WHERE snapReceiver = "+str(snapReceiver)+" AND snapStatus = 0;")

        deleteIDs = []
        snapsReceived = []

        for result in cur:
            deleteIDs.append(result[0])
            snapsReceived.append(result[1])

        return snapsReceived, deleteIDs

    def updateSnapStatus(self, userID):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("UPDATE snap SET snapStatus = 1 WHERE snapReceiver = "+str(userID)+";")
        conn.commit()
        cur.close()
        conn.close()

class User(SnapDB):

    def getUserID(self):
        IPAdd = self.getIPadress()
        print(IPAdd)


    def getUserInfo(self, userID):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("SELECT * ")


    # Deletes the relation that connects userID - friendID from the DB
    def deleteFriend(self, friendID):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute("DELETE FROM channel WHERE userID = "+str(self.userID)+" AND friendID = "+str(friendID)+";")
        conn.commit()
        cur.close()
        conn.close()





