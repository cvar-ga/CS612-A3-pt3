import xml.etree.ElementTree as ET
from json import loads
from sys import exit

#dtd = ET.ElementTree(file='students.dtd')
document = ET.ElementTree(file='students.xml')
root = document.getroot()
child_element = False
index = 0
child_elements = False
document_child = root.iter()
document_list = []
for child in document_child:
    document_list.append({'tag': child.tag, 'attrib': child.attrib})
    #print(child.tag, child.attrib)
with open('students.dtd', 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        if '<!ELEMENT' in line:
            element = line.split(' ')[1]
            if element != document_list[index]['tag']:
                print(element + ' != ' + document_list[index]['tag'] + ': XML is invalid. QUITTING!')
                exit()
            if '+' in line:
                child_element = line.split('(')[1].split('+')[0]
                index += 1
                continue

            if child_element:
                child_elements = line.split('(')[1].split(')')[0].split(', ')
                break
    for child in root.find(child_element):
        if child.tag in child_elements:
            continue
        else:
            print(child.tag + ' not in ' + child_element + ' element. XML is invalid. QUITTING!')
            exit()
print('XML is valid.')
