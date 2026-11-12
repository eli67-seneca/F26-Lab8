#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: class Dog

class Dog:
	def bark(self):
		"""Makes the dog park."""
		# each class method can access instance variables.
		return f"{self.dog_name} says woof!"

	def __init__(self, dog_name:str, dog_breed:str):
		"""Initialisation.\n
		`__init__` is the constructor. When created, it is called an *object of this
		class*. This constructor creates two variables, `dog_name` and `dog_breed`.
		These variables are called *attributes* or *instance variables*. Instance
		variables are created for each class object. Each class object receives its
		own instance variables.

		Args:
			dog_name (str): The name of the dog.
			dog_breed (str): The breed of the dog.
		"""
		self.dog_name = dog_name
		self.dog_breed = dog_breed