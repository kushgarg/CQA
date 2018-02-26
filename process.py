'''
from xml.dom import minidom

doc = minidom.parse("data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA-with-multiline.xml")
mainq = doc.getElementsByTagName("OrgQuestion")
relq = doc.getElementsByTagName("RelQBody")

for q in relq :
    print q.firstChild.data

'''


file = 'data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA-with-multiline.xml'

import xml.etree.ElementTree as ET
with open(file,'r') as xml_file:
    xml_file = ET.parse(xml_file)

import linecache as lc

'''fr = file.decode("utf-8").replace("<","")
tree = ET.parse(fr)'''
root = xml_file.getroot()

ftext = open('data/train_1.txt', 'w')
str1 = ""
for child in root.findall('.//RelQBody'):
    str1 = (str1 + str(child.text)).replace("&lt;","").replace("p&gt;","").replace("/","").replace("&amp;","").replace("#160;","").replace("&quot;","").replace("&nbsp;","").replace("b&gt;","")
    str2 = str1.replace('\n', '')
ftext.write(str1)
ftext.close()

print lc.getline('data/train_1.txt', 4)
print str2
