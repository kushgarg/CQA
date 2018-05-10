import RAKE
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

from difflib import SequenceMatcher

fh = open('C:\Users\sony\PycharmProjects\CQA\data\Comments.txt')
fl = open('C:\Users\sony\PycharmProjects\CQA\data\RelevantQues.txt')
cm = fh.readlines()
ques = fl.readlines()

q = ques[0]
print cm[0]
for i in range(0,10):
    q = q + cm[i]

q = q.replace('\n',' ')

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized.encode('utf8')

filet = open('data/test.txt','w')
qc = clean(q)
print(ques[0])
qt = clean(ques[0])
print qt
rake = RAKE.Rake(RAKE.SmartStopList())
r = rake.run(qt,minCharacters=3,maxWords=6)
print r
for i in range(0,10):
    c = clean(cm[i])
    print c
    r1 = rake.run(c,minCharacters=3,maxWords=5)
    print r1,SequenceMatcher(None,r1[0][0],qt).ratio()


a = "abcd abc xyz erty"
b = "abc"
print SequenceMatcher(None,a,b).ratio()
#kw = [rk for rk in r[i][0] for i in range(0,len(r))]
filet.write(str(r))

q = ques[1]
print q
for i in range(10,20):
    q = q + cm[i]

q = q.replace('\n',' ')

qc = clean(q)

qt = clean(ques[1])
print qt
rake = RAKE.Rake(RAKE.SmartStopList())
r = rake.run(qt,minCharacters=3,maxWords=6)
print r
for i in range(10,20):
    c = clean(cm[i])
    print c
    r1 = rake.run(c,minCharacters=3,maxWords=6)
    print r1
