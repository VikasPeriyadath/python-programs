import re
st=raw_input("enter site address : ")
p=re.compile("^[_A-Za-z0-9\^$.|?*]+"+
      ".co.in$")
s=p.match(st)
if s is None :
				print "     not Indian site"
else :
		print "     Indian site"