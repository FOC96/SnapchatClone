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

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

from connected import Connected
from login import Login


from DB_Connection import SnapDB

class Registrar(Screen):
    def do_registrar(self, userName, userNickName, userPassword):
        a = SnapDB()

        if userName == "" or userNickName == "" or userPassword == "":
            popup = Popup(title='Missing fields', content=Label(text='You\'re missing some fields, try again.'), size_hint=(None, None), size=(350, 200))
            popup.open()
        else:
            a.addUser(name=userName, nickName=userNickName, password=userPassword)
            app = App.get_running_app()

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'login'

    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""

    def regresar1(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'inicio'


class RegistrarApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Registrar(name='registrar'))
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

if __name__ == '__main__':
    RegistrarApp().run()
