#!/usr/bin/env python


import re,fileinput,string
from sys import stdin,stdout,stderr,argv
for line in stdin:
	m = re.search (argv[1], line)
	if m:
		print re.sub ('[%s]' % string.digits, argv[2], line)
#prints the grade twice, not sure why
