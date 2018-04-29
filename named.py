'''
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk import ne_chunk,pos_tag


text = "where can a person find massage oil in Qatar"

sents = sent_tokenize(text)
print(sents)

words = word_tokenize(text)
print(words)

print(nltk.pos_tag(words))

def ent(text):
    return ne_chunk(pos_tag(word_tokenize(text)))

tree = ent("when asked about the massage oil people told tht it can be found in Qatar easily")
print tree
'''

import os
java_path = "C:/Program Files/Java/jdk1.8.0_92/bin/java.exe"
os.environ['JAVAHOME'] = java_path

from nltk import sent_tokenize,word_tokenize
from nltk.tag import StanfordNERTagger
from nltk.tag.stanford import CoreNLPNERTagger

sn_7class = StanfordNERTagger('stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz',path_to_jar='stanford-ner-2018-02-27/stanford-ner.jar',encoding='utf8')

fh = open('data/RelevantQues.txt', 'r')
rq = fh.readlines()
fh = open('data/Comments.txt', 'r')
cm = fh.readlines()

for i in range(0,2):
    for j in range(0,10):
        k = j + i * 10

        cm[k] = cm[k].replace('"', '').replace('*', '').replace(';', '').replace('!', '').replace(':', '').replace(')','').replace('(', '').replace('?', '').replace('?', '').replace('_', '').replace('/', '').replace('=', '')
        cm[k] = cm[k].replace('.', ' ')

        rq[i] = rq[i].replace('"', '').replace('*', '').replace(';', '').replace('!', '').replace(':', '').replace(')','').replace('(', '').replace('?', '').replace('?', '').replace('_', '').replace('/', '').replace('=', '')
        rq[i] = rq[i].replace('.', ' ')

        tokens = cm[k].split(' ')
        tokens = filter(None, tokens)

        tokens1 = rq[i].split(' ')
        tokens1 = filter(None, tokens1)

        cner=[]
        qner=[]

        tup = sn_7class.tag(tokens)
        for t in tup:
            cner.append(t[1].encode("utf8"))

        tup = sn_7class.tag(tokens1)
        for t in tup:
            qner.append(t[1].encode("utf8"))

        cner = [x for x in cner if x!='O']
        qner = [x for x in qner if x != 'O']
        int = set(cner) & set(qner)

        print(int)




#print CoreNLPNERTagger(url='localhost:8080').tag('Rami Eid is studying at Stony Brook University in NY'.split())
