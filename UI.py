from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from Enums import LEGIONS
from Legion import Legion
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.relativelayout import RelativeLayout
class BuildButton(Button):
    text = "BUILD"


class HierarchyButton(BoxLayout):
    pass

class LegionButtons(BoxLayout):
    orientation = "vertical"
    buttons=[]
    activebutton=None
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        print("I am called")

        for legion in LEGIONS:
            button=Button(text=legion.name,on_release=self.activate)
            self.add_widget(button)
            self.buttons.append(button)

    def activate(self,button,**kwargs):
        for i in self.buttons:
            i.background_color=[1]*4
        button.background_color=(.5,1,.5,1)
        LegionBuilderApp.get_running_app().active_legion_button=LEGIONS[button.text]


class MenuWindow(Screen):
    pass

class ViewerWindow(Screen):
    active_leader=""
    active_title=""
    active_troop_count=0
    legion=None
    basewidget=ScatterLayout
    mainbox=BoxLayout
    _active=None

    def load(self,legion):
        self.mainbox=BoxLayout(orientation="vertical")
        self.legion=legion
        self.active=legion

        #for i in legion.

    @property
    def active(self):
        return self._active
    @active.setter
    def active(self,value):
        self._active=value
        self.active_title=value.main_title
        self.active_leader=value.leader_title
        self.active_troop_count=value.troop_count

class WindowManager(ScreenManager):
    pass

class LegionBuilderApp(App):
    legion=Legion
    active_legion_button=None
    wm=WindowManager
    menuscreen=MenuWindow
    viewerscreen=ViewerWindow


    def build(self):
        self.wm=WindowManager()
        self.menuscreen=MenuWindow()
        self.viewerscreen=ViewerWindow()
        self.wm.add_widget(self.menuscreen)
        self.wm.add_widget(self.viewerscreen)
        return self.wm
    def build_legion(self):
        self.legion=Legion()
        self.legion.populate(self.active_legion_button)
        self.viewerscreen.load(self.legion)





if __name__ == "__main__":
    app=LegionBuilderApp()
    app.run()