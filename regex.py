# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

a = 'Welcome to Python'
print(type(a))

s = 'woodchuck'

#[aA] matches a or A
#[A-Z] matches any character between A - Z
#[a-zA-Z] mathces any character irrespective of case
#[0-9] matches a single digit

re.search('[A-Z]', 'Apple Orange')
re.search('[O-Z]', 'Apple Orange')

#caret (^) is used to negate pattern in [] which means any character otherthan the pattern specified
#this is true only when ^ is the first symbol after []
re.search('[^aA]', 'Apple Orange')

# ? is used for "the preceding character or nothing"
re.search('apples?','apples')
re.search('[cC]olou?r','Color')

# * means zero or more occurances of previous character 
re.search('baaa*','baabaaa')
re.search('[ab]*','baabacaa')

re.search('343*','3430923')

# period (.) expression that matches any single character
re.search('beg.n','begin begun')
re.search('beg.','begun')

#Anchors: ^ matches start of a line and $ matches end of a line.
re.search('^The dog.$','The dog.')

re.search('cat|dog','cat or dog')
re.search('gupp(y|ies)','guppy guppies ')

re.search('(Column [0-9]+ *)*', 'Column 1 Column 2 Column 3')
re.search('the*','thethe')
re.search('(the)*','thethe')
re.search('(beg(in|un))*','begin begun')
re.search('[a-z]*','once upon')
re.search('$[0-9]+','$1000')
re.search(r'\b99\b','$99')

#5.5 GB
re.search(r'\b[0-9]+(\.[0-9]+)? (GB|[gG]igabytes?)\b','5 Gigabyte')

#specifications for >6GHz processor speed
re.search(r'\b[6-9]+ *(GHz|[Gg]igahertz)\b','6GHz')

#only matches more than 500 GB

