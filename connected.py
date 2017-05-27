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


from DB_Connection import SnapDB, Snap, User

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def capture(self):
        camera = self.ids['camera']

        # Naming snap
        timestr = time.strftime("%Y%m%d_%H%M%S")
        snapName = "Snap_{}.png".format(timestr)

        # Database registry !!FALTA SABER EL USERID DE QUIÉN LO MANDA Y A QUIÉN!!
        snap = Snap()
        snap.saveSnap(str(snapName), 1)

        # Saving file.png
        camera.export_to_png(snapName)

    #def close(self):
