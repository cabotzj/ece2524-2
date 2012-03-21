#!/usr/bin/env python
#prints the grade twice, not sure why

import re,fileinput,string

def grade_changer(data, name, grade)
	for line in data:
		m = re.search (name, line)
		if m:
			print re.sub ('[%s]' % string.digits, grade, line)
	return (data)

from sys import stdin,stdout,stderr,argv

if __name__=='__main__':

	(data) = grade_changer(stdin, argv[1], argv[2])
