import os

def saveUserInfoLocally(userID, userNickname, userName, userIPaddress):
    currentPath = os.getcwd()

    file = open(currentPath+"/userInfo/user.txt",'w')
    file.write(str(userID)+'\n')
    file.write(str(userNickname)+'\n')
    file.write(str(userName)+'\n')
    file.write(str(userIPaddress))
    file.close()

def getLocalUserInfo():
    currentPath = os.getcwd()

    file = open(currentPath+"/userInfo/user.txt",'r')
    content = file.readlines()

    userID = content[0].strip()
    userNickname = content[1].strip()
    userName = content[2].strip()
    userIPaddress = content[3].strip()

    return userID, userNickname, userName, userIPaddress
