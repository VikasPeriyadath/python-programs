import re
ph=raw_input("Enter Character : ")
u=re.compile("^[a-zA-Z]+$")
s=u.search(ph)
if s is None :
			print "Invalid "
else :
		print "Valid "