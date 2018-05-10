from gensim.models.keyedvectors import KeyedVectors
import math
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import xlwt
import datetime
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
file1 = 'data/input.word2vec'
model = KeyedVectors.load_word2vec_format(file1, binary=False)

#model = KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin',binary=True,limit=700000)

#fl = open('data/cs_sem.txt','w')

fh = open('data/GOLD_RelevantQues.txt', 'r')
rq = fh.readlines()
fh = open('data/GOLD_Comments.txt', 'r')
cm = fh.readlines()

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("LABELS")

sheet.write(0,0,"add_w2v")
sheet.write(0,1,"sub_w2v")
sheet.write(0,2,"cs_w2v")
sheet.write(0,3,"euc_w2v")
sheet.write(0,4,"man_w2v")

time = datetime.datetime.now()

for i in range(0,327):
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
        if k != 476 and k != 2548:
            for t in tokens:
                if not t in stop_words:
                    com.append(t)
        else:
            for t in tokens:
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

        add = sum(qv[x] + cv[x] for x in range(0, 100))
        add = add / 100

        sub = sum(abs(qv[x] - cv[x]) for x in range(0, 100))
        sub = sub / 100

        euc = math.sqrt(sum(pow(a - b, 2) for a, b in zip(qv, cv)))
        man = sum(abs(a - b) for a, b in zip(qv, cv))

        numerator = sum([qv[x] * cv[x] for x in range(0,100)])

        sum1 = sum([qv[x] ** 2 for x in range(0,100)])
        sum2 = sum([cv[x] ** 2 for x in range(0,100)])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            cs = 0.0
        else:
            cs = float(numerator) / denominator

        sheet.write(k+1, 0, add)
        sheet.write(k+1, 1, sub)
        sheet.write(k+1, 2, cs)
        sheet.write(k+1, 3, euc)
        sheet.write(k+1, 4, man)
        print k

book.save('data/GOLD_w2v.xls')
#fl.close()
fh.close()
print datetime.datetime.now() - time

'''
from gensim.scripts.glove2word2vec import glove2word2vec
file = 'data/word2vector.txt'
file1 = 'data/input.word2vec'
glove2word2vec(file,file1)
'''
#file1 = 'data/input.word2vec'
#model = KeyedVectors.load_word2vec_format(file1, binary=False)
# calculate: (king - man) + woman = ?
#result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#print(result)
#model = KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin',binary=True,limit=700000)

#print len(model['king'])