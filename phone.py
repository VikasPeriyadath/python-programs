import re
ph=raw_input("Enter Phone number : ")
u=re.compile("^[789]\d{9}$")
s=u.search(ph)
if s is None :
			print "Invalid "
else :
		print "Valid "