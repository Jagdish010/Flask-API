# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import math

def fact(n):
	fact = 1
	
	fact_list = range(1, n+1)
	for i in fact_list:
		fact = fact * i
	
	print('factorial of {} is {} = {}'.format(n, ' * '.join(map(str, fact_list)), fact))



if __name__ == '__main__':
	while True:
		val = input("Enter your value: ")

		if type(val) == int:
			# print(math.factorial(int(val)))
			fact(int(val))
		else:
			print('Value should be of type int not {}'.format(type(val)))