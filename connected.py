import kivy
kivy.require('1.0.6')
from kivy.app import App
from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

import time

import ImageFunctions
import localFiles
from DB_Connection import SnapDB, Snap, User

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def capture(self, option, snapReceiver):
        camera = self.ids['camera']

        if snapReceiver != "" and snapReceiver != None:

            # Naming snap
            timestr = time.strftime("%Y%m%d_%H%M%S")
            snapName = "Snap_{}.png".format(timestr)

            # Saving file.png
            camera.export_to_png(snapName)

            # Database registry !!FALTA SABER EL USERID DE QUIÉN LO MANDA Y A QUIÉN!!
            snap = Snap()
            snap.saveSnap(snapName=str(snapName), snapSender=localFiles.getLocalUserInfo()[0], snapFile="\""+str(ImageFunctions.imageToText(snapName)).strip()+"\"", snapReceiver=snapReceiver)

            path = os.getcwd()
            path = path+"/"+snapName

            if option == 1:
                print("NORMAL")
            elif option == 2:
                print("GRAYSCALE")
                ImageFunctions.editar3(path)
            elif option == 3:
                print("SEPIA")
                ImageFunctions.editar2(path)
            elif option == 4:
                print("BLUR")
                ImageFunctions.editar1(path)

        else:
            popup = Popup(title='Oh', content=Label(text='It seems like you forgot to tell who this snap will be sent to (userID).'), size_hint=(None, None), size=(550, 200))
            popup.open()

    def checkSnapInbox(self):
        try:
            print("Looking for snaps...")
            a = Snap()
            namesFound = a.getImageName(localFiles.getLocalUserInfo()[0])[0]
            idsFound = a.getImageName(localFiles.getLocalUserInfo()[0])[1]

            if len(namesFound) == 0:
                popup = Popup(title='Oops!', content=Label(text='There are no new snaps for you, '+localFiles.getLocalUserInfo()[2].split(" ")[0]), size_hint=(None, None), size=(350, 200))
                popup.open()
            else:
                for x in range(len(namesFound)):
                    img = str(namesFound[x]).strip()
                    ImageFunctions.showImg(img)
                a.updateSnapStatus(localFiles.getLocalUserInfo()[0])
        except:
            print("ERROR")

    def signOut(self):
        localFiles.saveUserInfoLocally(userID=0, userIPaddress=0, userName="No name", userNickname="No Nickname")
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'inicio'
