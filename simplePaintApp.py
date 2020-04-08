# https://kivy.org/doc/stable/tutorials/firstwidget.html

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class Point(Widget):
	with self.canvas:
		Color(random(), 1, 1)
		d = 15
		Ellipse(pos = self.center)


class MyPaintWidget(Widget):

	def on_touch_down(self, touch):
		touch.grab(self)
		color = (random(), 1, 1)
		with self.canvas:
			Color(*color, mode='hsv')
			d = 15.
			Ellipse(pos = (touch.x - d/2, touch.y - d/2), size=(d, d))
			touch.ud['endpoints'] = {'d':d}
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=1.05)

	def on_touch_move(self, touch):
		if(touch.grab_current is self):
			with self.canvas:
				initial_points = touch.ud['line'].points[0:2]
				touch.ud['line'].points.clear()
				touch.ud['line'].points = [initial_points[0], initial_points[1], touch.x, touch.y]

	def on_touch_up(self, touch):
		if(touch.grab_current is self):
			with self.canvas:
				d = touch.ud['endpoints']['d']
				Ellipse(pos = (touch.x - d/2, touch.y - d/2), size=(d, d))



class MyPaintApp(App):

	def build(self):
		parent = Widget()
		self.painter = MyPaintWidget()
		clearbtn = Button(text='Clear')
		clearbtn.bind(on_press=self.clear_canvas)
		parent.add_widget(self.painter)
		parent.add_widget(clearbtn)
		return parent

	def clear_canvas(self, obj):
		self.painter.canvas.clear()


if __name__ == '__main__':
	MyPaintApp().run()
		