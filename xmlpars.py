from xml.dom import minidom
xmldoc = minidom.parse('data.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value,s.attributes['name'].nodeName)

#print dir(s.attributes['name'])

