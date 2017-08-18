# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def combinations(elems, s, idx, result):
	for i in range(idx, len(elems)):
		s+=elems[i]
		result.append(s)
		combinations(elems, s, i+1, result)
		s=s[0:-1]

result = []
combinations('123', '', 0, result)
print result
