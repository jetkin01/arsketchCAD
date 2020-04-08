#First attempt to create my own Kivy sketching app

from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MainGraphicWindow(GridLayout):
    
    def __init__(self, **kwargs):
    	super(MainGraphicWindow, self).__init__(**kwargs)
    	self.cols = 1
    	self.draw_here_prompt = Label(text="draw here")
    	self.add_widget(self.draw_here_prompt)



class sketchr(App):

    def build(self):
        return MainGraphicWindow()

if __name__ == "__main__":
    sketchr().run()