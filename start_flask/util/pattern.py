# -*- coding: utf-8 -*-

from __future__ import unicode_literals


# *
# *    *
# *    *    *
# *    *    *    *
# *    *    *    *    *


def pattern1():
	for i in range(0, 5):
		print("    ".join(list("*"*int(i + 1))))



# *
# *    *
# *    *    *
# *    *    *    *
# *    *    *    *
# *    *    *
# *    *
# *


def pattern2(rev=False):
	_min, _max, rev_ord = 0, 4, 1
	if rev:
		_min, _max, rev_ord = 3, -1, -1

	for i in range(_min, _max, rev_ord):
		print("    ".join(list("*"*int(i + 1))))
	
	if rev: return

	pattern2(True)



if __name__ == '__main__':
	print("Assignment pattern 1 \n")
	pattern1()
	print("Assignment pattern 2 \n")
	pattern2()