#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: Models an *actual* cash register.

class CashRegister:
	items = []
	total = 0.0

	@property
	def item_count(self):
		return len(self.items)

	def add_item(self, name:str, price:float):
		"""Adds an item to the cart

		Args:
			name (str): Name of the item
			price (float): Price of the item
		"""
		item = {"name": name, "price": price}
		self.items.append(item)
		self.total += price
		print(f"Added {name} for ${price:.2f}")

	def display_items(self):
		"""Displays all items in the cart."""
		print("\nItems in cart:")
		for item in self.items:
			print(f"- {item['name']}: ${item['price']:.2f}")
		print(f"Total: ${self.total:2f}\n")

	def undo(self):
		last_item = self.items.pop()
		self.total -= last_item['price']
		print(f"Removed {last_item['name']} (${last_item['price']})")

	def checkout(self, payment:float):
		"""Handle payments and calculates change.
		
		Args:
			payment (float): Amount paid by customer
		"""
		if payment < self.total:
			print("Insufficient payment. Please pay more.")
			return

		change = payment - self.total
		print(f"Payment accepted. Change: ${change:.2f}")
		self.reset()
	
	def reset(self):
		"""Clear the cart and reset total."""
		self.items = []
		self.total = 0.0