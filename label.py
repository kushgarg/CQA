import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")
'''
file = 'data/SemEval2016-Task3-CQA-QL-test-subtaskA.xml'

import xml.etree.ElementTree as ET
with open(file,'r') as xml_file:
    xml_file = ET.parse(xml_file)

root = xml_file.getroot()
file = open('data/GOLD_Labels.txt', 'w')
str1 = ""

for child in root.findall('.//RelComment'):
    json_str = json.dumps(child.attrib)
    resp = json.loads(json_str)
    str1 = str1 + str(resp['RELC_RELEVANCE2RELQ']) + '\n'

file.write(str1)
file.close()

'''
#fh = open('data/RelevantQues.txt', 'r')
#rq = fh.readlines()
#fh = open('data/GOLD_Comments.txt', 'r')
#cm = fh.readlines()
'''
import ngram
print ngram.NGram.compare(rq[0],cm[0])
print rq[1998]
print cm[19989]
'''

#com = ""
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words.remove("no")

r1 = "None"
for r in stop_words:
    if r == r1:
        print r1



