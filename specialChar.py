import re
ph=raw_input("Enter Character : ")
u=re.compile("^[&\\-()]+$")
s=u.search(ph)
if s is None :
			print "Invalid "
else :
		print "Valid "