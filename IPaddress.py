import re
st=raw_input("enter IP address : ")
p=re.compile("^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])$")
s=p.match(st)
if s is None :
				print "     Invalid IP address"
else :
		print "     valid IP address"