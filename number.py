import re
ph=raw_input("Enter Number : ")
u=re.compile("^\d+$")
s=u.search(ph)
if s is None :
			print "Invalid "
else :
		print "Valid "