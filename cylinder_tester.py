#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: Test cylinder.py

from cylinder import Cylinder

def main():
	height = 1000
	radius = 10

	cylinder = Cylinder(height, radius)
	v = cylinder.volume()
	s = cylinder.surface_area()

	out = "CYLINDER TESTER\n"
	out += f"Input parameters\n"
	out += f"Height:\t\t{height:,}\n"
	out += f"Radius:\t\t{radius:,}\n"
	out += f"\nCalculated values:\n"

	out += f"Volume:\t\t{v:,.3f}\n"
	out += f"Surface area:\t{s:,.3f}\n"
	out += f"Top area:\t{cylinder.top}"

	print(out)

if __name__ == "__main__":
	main()