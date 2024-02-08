import sys

"""
Aim: this script counts the numbers of lines in standeard input
+Input: string form the command line
Author: N.Ameele
"""

count = 0 

for line in sys.stdin:
	count += 1 

 print(count, "lines in  standard input")

