'''
from xml.dom import minidom

doc = minidom.parse("data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA-with-multiline.xml")
mainq = doc.getElementsByTagName("OrgQuestion")
relq = doc.getElementsByTagName("RelQBody")

for q in relq :
    print q.firstChild.data

'''
import sys
reload(sys)
sys.setdefaultencoding("utf8")

file = 'data/SemEval2016-Task3-CQA-QL-test-subtaskA.xml'

import xml.etree.ElementTree as ET
with open(file,'r') as xml_file:
    xml_file = ET.parse(xml_file)

root = xml_file.getroot()

ftext = open('data/GOLD_RelevantQues.txt', 'w')
str1 = ""
for child in root.findall('.//RelQBody'):
    str1 = (str1 + str(child.text).replace('\n', '') + '\n').replace("&lt;","").replace("p&gt;","").replace("/","").replace("&amp;","").replace("#160;","").replace("&quot;","").replace("&nbsp;","").replace("b&gt;","")
ftext.write(str1)
ftext.close()

'''ftext = open('data/MainQues.txt', 'w')
str1 = ""
for child in root.findall('.//OrgQBody'):
    str1 = (str1 + str(child.text) + '\n')

ftext.write(str1)
ftext.close()
'''
ftext = open('data/GOLD_Comments.txt', 'w')
str1 = ""
for child in root.findall('.//RelCText'):
    str1 = (str1 + str(child.text) + '\n')

ftext.write(str1)
ftext.close()

