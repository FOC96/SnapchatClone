import userSettings

def saveInfo(userID, userNickname, userName):
    userSettings.savedUserInfo.append(userID, userNickname, userName)
