import xml.etree.ElementTree as ET
from json import loads

document = ET.ElementTree(file='students.xml')
schema = ET.ElementTree(file='students.xsd')
document_root = document.getroot()
schema_root = schema.getroot()
index = 0
document_list = []
schema_list = []
document_child = document_root.iter()
for child in document_child:
    document_list.append({'tag': child.tag, 'attrib': child.attrib})
    #print(child.tag, child.attrib)
for child in schema_root.iter():
    if not child.attrib:
        continue
    else:
        schema_list.append(child)

schema_list = schema_list[:-1]
for child in schema_list:
    if child.attrib['name'] == document_list[index]['tag']:
        print(child.attrib['name'] + ' tag is valid.')
    else:
        print(child.attrib['name'] + ' tag is invalid. XML invalid. QUITTING!')
        break
    index += 1
