import xml.etree.ElementTree as ET

file = 'data/SemEval2016-Task3-CQA-QL-train-part1-subtaskA-with-multiline.xml'
tree = ET.parse(file)
root = tree.getroot()

ftext = open('data/train_1.txt', 'w')
str1 = ""
for child in root.findall('.//RelQBody'):
    str1 = str1 + str(child.text)

ftext.write(str1)
ftext.close()
