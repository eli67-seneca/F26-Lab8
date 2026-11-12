#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: Tests `cashregister.py`
from cashregister import CashRegister

def pprint(cr:CashRegister):
	print(f"Items:\t{cr._item_count}\nTotal:\t${cr._total_price}\n")

def main():
	c = CashRegister()
	c.add_item(10)
	pprint(c)

	c.add_item(25)
	pprint(c)

	c.add_item(15)
	pprint(c)

	c.undo()
	pprint(c)

if __name__ == "__main__":
	main()