import xml.etree.ElementTree as ET

mytree=ET.parse(".\Boat Landing_20230831.xml")

myroot=mytree.getroot()

print(myroot.tag)

print(myroot[4].tag)

#print(myroot[0].attrib)