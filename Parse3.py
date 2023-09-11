import xml.etree.ElementTree as ET

# Sample XML data
xml_data = '''
<bookstore>
    <book>
        <title>Python Programming</title>
        <author>John Smith</author>
        <price>29.99</price>
    </book>
    <book>
        <title>Data Science Essentials</title>
        <author>Jane Doe</author>
        <price>39.99</price>
    </book>
</bookstore>
'''

# Parse the XML data
root = ET.fromstring(xml_data)
print(root.tag)

# Access elements and attributes
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    price = book.find('price').text
    print(f"Title: {title}, Author: {author}, Price: {price}")