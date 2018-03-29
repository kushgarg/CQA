import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")

file = 'data/SemEval2016-Task3-CQA-QL-train-part1.xml'

import xml.etree.ElementTree as ET
with open(file,'r') as xml_file:
    xml_file = ET.parse(xml_file)

root = xml_file.getroot()
file = open('data/Labels_RelComm.txt', 'w')
str1 = ""

for child in root.findall('.//RelComment'):
    json_str = json.dumps(child.attrib)
    resp = json.loads(json_str)
    str1 = str1 + str(resp['RELC_RELEVANCE2RELQ']) + '\n'

file.write(str1)
file.close()