# Geometry.py
#
#	Implements basic geometrical objects:
#		- Point
#		-
#

from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from random import random

class Point(Widget):
	""" 0-dimensional Point Widget"""
	def __init__(self, canvas, **kwargs):
		super(Point, self).__init__(**kwargs)
		self.color = Color(random(), 1, 1, mode="hsv")
		self.canvas = canvas
		self.x = 0
		self.y = 0
		self.diameter = 15

	def display(self):
		with self.canvas:
			Color = self.color
			d = self.diameter
			x = self.x
			y = self.y
			Ellipse(pos = (x - d/2, y - d/2), size=(d, d))
			
	def on_move(self, touch):
		if (touch.grab_current is self):
			self.diameter *= 1.5
			self.display(self)


class Plane(ScatterLayout):
	"""2D Plane Widget"""
	def __init__(self, **kwargs):
		super(Plane, self).__init__()
		self.points = []

	def on_touch_down(self, touch):
		touch.grab(self)
		indx = len(self.points)
		self.points.append(Point(self.canvas))
		self.points[0].x = touch.x
		self.points[0].y = touch.y
		with self.canvas:
			self.points[0].display()


		