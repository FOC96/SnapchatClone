import pymysql
import socket


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


    # Gets the device's IP Address
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

        cur.execute("INSERT INTO user(userNickname, userName, userPassword, userIPAddress) VALUES('"+nickName+"', '"+name+"', '"+password+"', '"+self.getIPadress()+"');")

        # Changes are saved through 'commit()'
        conn.commit()
        cur.close()
        conn.close()


    # DEFS YET TO BE UPDATED!!

    def getAllArtists(self):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM artist ORDER BY artistID")
        for row in cur:
            print(row)

        cur.close()
        conn.close()



    def getAllSongs(self):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute("SELECT song.songID, song.songName, artist.artistName, album.albumTitle, genre.genreName FROM album, artist, genre, song WHERE song.songArtist = artist.artistID AND song.songAlbum = album.albumID AND song.songGenre = genre.genreID ORDER BY song.songID;")

        for row in cur:
            print(row)

        cur.close()
        conn.close()


a = snapDB()
a.addUser("loco12", "Juan Gabriel", "contra123")
