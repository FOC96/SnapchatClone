from DB_Connection import SnapDB
from DB_Connection import Snap
from DB_Connection import User
from DB_Connection import Channel

import time


a = SnapDB()
u3 = User(a.checkLogin("user3", "passTres"))
u3.deleteFriend("4")
