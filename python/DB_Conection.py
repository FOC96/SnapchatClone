import socket
import pymysql

#Variables de DB
db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_password = ''
db_charset = 'utf8'
db_database = 'waves'

#
conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_password, db=db_database)
cur = conn.cursor()

cur.execute("SELECT song.songID, song.songName, artist.artistName, album.albumTitle, genre.genreName FROM album, artist, genre, song WHERE song.songArtist = artist.artistID AND song.songAlbum = album.albumID AND song.songGenre = genre.genreID;")

print("Existen", cur.rowcount, "artistas")

for row in cur:
    print(row)

cur.close()
conn.close()


# NOTAS:
# Se cambiará la base de datos, la que se emplea es para pruebas de funcionamiento

class connection:

    def getConnection(self):
        conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_password, db=db_database)
        return conn

    def addNewUser(self, name, password, ipAddress):
        cur = conn.cursor()
        cur.execute("INSERT into ")
