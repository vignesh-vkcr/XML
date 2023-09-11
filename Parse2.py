import xml.sax

class GroupHandler(xml.sax.ContentHandler):
	"""docstring for GroupHandler"""
	def startElement(self, name, attrs):
		#print(name)
		pass

	def characters(self, content):
		#print(content)
		pass

	def endElement(self, name):
		print(name)
		pass

handler=GroupHandler()
parser=xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("Boat Landing_20230831.xml")  