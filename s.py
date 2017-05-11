import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('data.xml').getroot()

for child in e:
	   print(child.tag, child.attrib)

