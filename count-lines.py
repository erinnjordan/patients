""" This script counts the number of lines in a standard input.
Input: strings from the system's standard input
"""

import sys

count= 0
for line in sys.stdin:
	count+=1
print(count, 'Total lines in standard input.')


