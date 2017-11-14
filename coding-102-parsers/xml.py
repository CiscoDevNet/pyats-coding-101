'''
Parsing XML
-----------

Python features a built-in module named 'xml' that facilitates the parsing and
constructuring of XML. Alternatively, you could also use the PyPI 'lxml' 
package, a more powerful xml parser.

For simplicity, this example uses only built-in python xml module.

Read more at https://docs.python.org/3/library/xml.html
             http://lxml.de/
'''

import xml

XML_STRING = '''
<data>
    <character name="blackwidow">
        <firstname>natasha</firstname>
        <lastname>romanoff</lastname>
    </character>
    <character name="ironman">
        <firstname>tony</firstname>
        <lastname>stark</lastname>
    </character>
</data>
'''
from xml.etree import ElementTree

# parse into root
root = ElementTree.fromstring(XML_STRING)

root.tag        
# 'data'

for child in root:
    print(child.tag, child.attrib)
    print("    ", child[0].tag, child[0].text)
    print("    ", child[1].tag, child[1].text)
# character {'name': 'blackwidow'}
#      firstname natasha
#      lastname romanoff
# character {'name': 'ironman'}
#      firstname tony
#      lastname stark

