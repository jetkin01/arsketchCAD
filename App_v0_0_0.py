# https://kivy.org/doc/stable/tutorials/firstwidget.html

from random import random
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
# HoverBehavior
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window

from Geometry import Point, Plane

class HoverBehavior(object):
	# From: https://docs.google.com/viewer?a=v&pid=forums&srcid=MTU1MzAwMDk1MDk2MDU2OTc1NDcBMDc5ODU1NzgyMDU1MDYyNzc3MDEBeVE4MTZ6djBqeTRKATAuMQEBdjI&authuser=0
	hovered = BooleanProperty(False)
	border_point = ObjectProperty(None)

	def __init__(self, **kwagrs):
		self.register_event_type('on_enter')
		self.register_event_type('on_leave')
		Window.bind(mouse_pos=self.on_mouse_pos)
		super(HoverBehavior, self).__init__(**kwargs)

	def on_mouse_pos(self, *args):
		pos = args[1]
		inside = self.collise_point(*pos)
		if self.hovered == inside:
			return
		self.border_point = pos
		self.hovered = inside
		if inside:
			self.dispatch('on_enter')
		else:
			self.dispatch('on_leave')

	def on_enter(self):
		pass

	def on_leave(self):
		pass



# class InertialPlane(Widget):

# 	def __init__(self, **kwargs):
# 		super(InertialPlane, self).__init__(**kwargs)
# 		self.prompt = Label(text="draw here")
# 		self.valign = 'middle'
# 		self.layout = AnchorLayout()
# 		self.layout.add_widget(self.prompt)

# 	def on_touch_down(self, touch):
# 		touch.grab(self)
# 		color = (random(), 1, 1)
# 		self.startPoint = Point(self.canvas)
# 		self.startPoint.x = touch.x
# 		self.startPoint.y = touch.y
# 		self.startPointColor = color
# 		with self.canvas:
# 			Color = color
# 			self.startPoint.display()
# 			touch.ud['line'] = Line(points=(touch.x, touch.y), width=1.05)

# 	def on_touch_move(self, touch):
# 		if(touch.grab_current is self):
# 			with self.canvas:
# 				initial_points = touch.ud['line'].points[0:2]
# 				touch.ud['line'].points.clear()
# 				touch.ud['line'].points = [initial_points[0], initial_points[1], touch.x, touch.y]

# 	def on_touch_up(self, touch):
# 		if(touch.grab_current is self):
# 			self.endPoint = Point(self.canvas)
# 			self.endPoint.x = touch.x
# 			self.endPoint.y = touch.y
# 			self.endPoint.color = self.startPoint.color
# 			with self.canvas:
# 				Color = self.endPoint.color
# 				self.endPoint.display()



class MyPaintApp(App):

	def build(self):

		parent = Widget()

		self.plane = Plane()
		parent.add_widget(self.plane)
		self.prompt = Label(
			text="click to draw", 
			pos_hint = {'top':5, 'right':2})
		parent.add_widget(self.prompt)

		clearbtn = Button(text='Clear')
		clearbtn.bind(on_press=self.clear_canvas)
		parent.add_widget(clearbtn)

		return parent

	def clear_canvas(self, obj):
		self.plane.canvas.clear()


if __name__ == '__main__':
	MyPaintApp().run()
		