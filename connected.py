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

        # Naming snap
        timestr = time.strftime("%Y%m%d_%H%M%S")
        snapName = "Snap_{}.png".format(timestr)

        # Saving file.png
        camera.export_to_png(snapName)

        # Database registry !!FALTA SABER EL USERID DE QUIÉN LO MANDA Y A QUIÉN!!
        snap = Snap()
        snap.saveSnap(snapName=str(snapName), snapSender=localFiles.getLocalUserInfo()[0], snapFile="\""+str(ImageFunctions.imageToText(snapName)).strip()+"\"", snapReceiver=snapReceiver)

        if option == 1:
            print("NORMAL")
        elif option == 2:
            print("GRAYSCALE")
        elif option == 3:
            print("SEPIA")
        elif option == 4:
            print("BLUR")

        ##aqui termina el abrir ventana

    def checkSnapInbox(self):
        print("BUSCANDO SNAPS")
