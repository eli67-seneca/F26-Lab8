#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: Models a cash register used in supermarkets.

class CashRegister:
	def __init__(self):
		self._item_count = 0
		self._total_price = 0.0
		self._history = []
			  
	def add_item(self, price):
		self._item_count += 1
		self._total_price += price
		self._history.append(price)
		
	def get_total(self):
		return self._total_price

	def get_count(self):
		return self._item_count
	
	def clear(self):
		self._item_count = 0
		self._total_price = 0.0
		self._history = []
		
	def undo(self):
		self._item_count -= 1
		self._total_price -= self._history.pop()
