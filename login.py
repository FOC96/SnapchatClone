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
import localFiles
from connected import Connected
import userSettings

from DB_Connection import SnapDB

class Login(Screen):
    def do_login(self, loginText, passwordText):
        a = SnapDB()
        val = a.checkLogin(nickname=loginText, password=passwordText)
        userID = val[1]

        if val[1] != None:
            a = SnapDB()
            a.getUserData(userID)

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

        app = App.get_running_app()

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""

    def regresar(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'inicio'

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
