from gensim.models import Word2Vec
import math
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

'''
fh = open('C:\Users\sony\PycharmProjects\CQA\data\Comments.txt')
fl = open('C:\Users\sony\PycharmProjects\CQA\data\RelevantQues.txt')
cm = fh.read()
ques = fl.read()

cm = cm.replace('"', '').replace('*', '').replace(';', '').replace('!','').replace(':','').replace(')','').replace('(','').replace('?','').replace('?','').replace('_','').replace('/','').replace('=','')
cm = cm.replace('.',' ')

ques = ques.replace('"', '').replace('*', '').replace(';', '').replace('!','').replace(':','').replace(')','').replace('(','').replace('?','').replace('?','').replace('_','').replace('/','').replace('=','')
ques = ques.replace('.',' ')

tokens = cm.split(' ')
tokens = filter(None,tokens)

tokens1 = ques.split(' ')
tokens1 = filter(None,tokens1)


cm = ' '.join(tokens)
cm = cm.replace('\n',' ')
tokens = cm.split(' ')

ques = ' '.join(tokens1)
ques = ques.replace('\n',' ')
tokens1 = ques.split(' ')


com=[]
for t in tokens:
    if not t in stop_words:
        com.append(t)

qt=[]
for t in tokens1:
    if not t in stop_words:
        qt.append(t)


list = com + qt
list = [list]

model = Word2Vec(list,min_count=1,size=100,workers=4)
model.save('data/vectors_QC')
'''

model = Word2Vec.load('data/vectors_QC')

fl = open('data/cs_sem.txt','w')

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

        com = []
        for t in tokens:
            if not t in stop_words:
                com.append(t)

        qt = []
        for t in tokens1:
            if not t in stop_words:
                qt.append(t)

        qv = [0]*100
        cv = [0]*100

        for v in range(0,100):
            for q in qt:
                try:
                    qv[v] = qv[v] + model[q][v]
                except KeyError:
                    qv[v] = qv[v] + 0
            qv[v] = qv[v]/(len(qt))

        for v in range(0,100):
            for c in com:
                try:
                    cv[v] = cv[v] + model[c][v]
                except KeyError:
                    cv[v] = cv[v] + 0.0
            cv[v] = cv[v]/(len(com))

        numerator = sum([qv[x] * cv[x] for x in range(0,100)])

        sum1 = sum([qv[x] ** 2 for x in range(0,100)])
        sum2 = sum([cv[x] ** 2 for x in range(0,100)])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            cs = 0.0
        else:
            cs = float(numerator) / denominator

        fl.write(str(cs)+'\n')

fl.close()
fh.close()
