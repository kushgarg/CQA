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

text = """Yes. It is right behind Kahrama in the National area.
whats the name of the shop?
It's called Naseem Al-Nadir. Right next to the Smartlink shop. You'll find the chinese salesgirls at affordable prices there.
dont want girls;want oil
Try Both ;) I'am just trying to be helpful. On a serious note - Please go there. you'll find what you are looking for.
you mean oil and filter both
Yes Lawa...you couldn't be more right LOL
What they offer?
FU did u try with that salesgirl ?
Swine - No I don't try with salesgirls. My taste is classy ;)
Most massages in Qatar are a waste of money. All they do is just rub some oil. No body does deep tissue massage here.
my masseuse is very good. calling her from to time for home service. currently in the philippines for a month vacation; i guess. =( she is the best in aromatherapy massage.
there is a massage center near mall roundabout in hilal opp. to woqood petrol station
Try Magic Touch in Abu Hamour (beside Abu Hamour Petrol Stn)it will just cost you 60QR per hour and I've seen a lot of Qataris as their customers.
Can anybody recommend a good place for head massages? I am constantly getting migranes and would like a head massage after the medication has done its job as I am left very drained. Thank you :)
call them they are good 44410410.
Hi Roy; what place is the contact number for that you posted?"""

sentences = sent_tokenize(text)
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

print sentences

sn_4class = StanfordNERTagger('stanford-ner-2018-02-27/classifiers/english.muc.7class.distsim.crf.ser.gz',path_to_jar='stanford-ner-2018-02-27/stanford-ner.jar',encoding='utf8')
ne_annot_sent_4c = [sn_4class.tag(sent) for sent in tokenized_sentences]

print ne_annot_sent_4c

#print CoreNLPNERTagger(url='localhost:8080').tag('Rami Eid is studying at Stony Brook University in NY'.split())
