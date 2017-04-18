from DB_Connection import User
from DB_Connection import SnapDB
from DB_Connection import Snap
from DB_Connection import Channel

a = SnapDB()
u1 = a.checkLogin("foc96", "contra123")

if u1 != None:
    user1 = User(u1)
    print(user1.userID, user1.userName, user1.userNickname, user1.userPassword, user1.userIPAddress)

