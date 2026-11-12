#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-11-10
# Purpose: To test the `Dog` class in dog.py

from dog import Dog

def main():
	my_dog = Dog("Minty", "Maltipoo")
	woof = my_dog.bark()

	print(woof)

if __name__ == "__main__":
	main()
