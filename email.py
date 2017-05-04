import re
st=raw_input("enter email : ")
p=re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*"+
      "@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
s=p.match(st)
if s is None :
				print "     Invalid Email"
else :
		print "     Valid Email"