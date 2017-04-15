# DB connection
import pymysql
# To get the device's IP address
import socket
# Password encryption
from passlib.hash import pbkdf2_sha256


class snapDB:
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
            check = pbkdf2_sha256.verify(password, element[3])

            if check == True and element[1] == nickname:
                session = True
                name = element[2]
                userID = element[0]
                break
        cur.close()
        conn.close()

        if session == True:
            print("Sesión iniciada con éxito,", name)
            return userID
        else:
            print("Error en los campos")





a = snapDB()
#a.addUser("john1", "Juan", "passOn")
user = a.checkLogin("john1", password="passOn")
print(user)
