import localFiles
from DB_Connection import SnapDB

a = SnapDB()
print(a.getUserData(7))

localFiles.saveUserInfoLocally(a.getUserData(7)[0], a.getUserData(7)[1], a.getUserData(7)[2], a.getUserData(7)[3])
