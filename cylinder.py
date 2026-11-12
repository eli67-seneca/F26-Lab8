#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: class Cylinder
from math import pi as PI

class Cylinder:
	def volume(self) -> float:
		"""Returns its volume

		Returns:
			float: The volume of itself
		"""
		return self.top * self.height
	
	def surface_area(self) -> float:
		"""Returns surface area

		Returns:
			float: Surface area
		"""
		return (2 * self.top) + (2 * PI * self.radius * self.height)

	@property
	def top(self) -> float:
		"""Returns the area of the top of the cylinder.

		Returns:
			float: The area at the top of the cylinder
		"""
		return PI * self.radius ** 2

	@property
	def circ(self) -> float:
		"""Returns the circumference of the cylinder.

		Returns:
			float: The circumference of the cylinder.
		"""
		return PI * self.diameter
	
	def __init__(self,height:float=1, radius:float=1) -> None:
		self.height = height
		self.radius = radius
		self.diameter = radius * 2
		
