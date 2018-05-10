import sys
reload(sys)
sys.setdefaultencoding("utf8")
import gensim
from gensim import corpora
import datetime
import math
import xlwt
from gensim.test.utils import common_corpus, common_dictionary
'''
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

# compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]
'''
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized.encode('utf8')

#doc_clean = [clean(doc).split() for doc in doc_complete]
#print doc_clean

fh = open('data/RelevantQues.txt', 'r')
rq = fh.readlines()
fh = open('data/Comments.txt', 'r')
cm = fh.readlines()

doc_complete =[]
time = datetime.datetime.now()

for i in range(0,1999):
    doc_complete.append(rq[i])
    for j in range(0,10):
        k = j + i * 10
        doc_complete.append(cm[k])

doc_clean = [clean(doc).split() for doc in doc_complete]
dict = corpora.Dictionary(doc_clean)
matrix = [dict.doc2bow(doc) for doc in doc_clean]

ldamallet = gensim.models.wrappers.LdaMallet(mallet_path='c:/mallet/bin/mallet',corpus=matrix,num_topics=10,id2word=dict)
ldamallet.save('data/mal.lda')

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("LABELS")

sheet.write(0,0,"add_lda")
sheet.write(0,1,"sub_lda")
sheet.write(0,2,"cs_lda")
sheet.write(0,3,"euc_lda")
sheet.write(0,4,"man_lda")
count=1

for i in range(0,21989,11):
    for j in range(0,10):

        k = i+j+1
        q=[]
        c=[]
        for n in range(0,10):
            q.append(ldamallet[matrix][i][n][1])
        for n in range(0,10):
            c.append(ldamallet[matrix][k][n][1])

        add = sum(q[x]+c[x] for x in range(0,10))
        add = add/10

        sub = sum(abs(q[x]-c[x]) for x in range(0,10))
        sub = sub/10

        euc = math.sqrt(sum(pow(a-b,2) for a,b in zip(q,c)))
        man = sum(abs(a-b) for a,b in zip(q,c))
        numerator = sum([q[x] * c[x] for x in range(0, 10)])

        sum1 = sum([q[x] ** 2 for x in range(0, 10)])
        sum2 = sum([c[x] ** 2 for x in range(0, 10)])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            cs = 0.0
        else:
            cs = float(numerator) / denominator

        sheet.write(count,0,add)
        sheet.write(count,1,sub)
        sheet.write(count,2,cs)
        sheet.write(count,3,euc)
        sheet.write(count,4,man)

        count = count+1

book.save('data/trail1.xls')
print datetime.datetime.now() - time