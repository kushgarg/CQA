from __future__ import division
import math
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

fh = open('C:\Users\sony\PycharmProjects\CQA\data\Comments.txt')
cm = fh.read()

cm = cm.replace('"', '').replace('*', '').replace(';', '').replace('!','').replace(':','').replace(')','').replace('(','').replace('?','').replace('?','').replace('_','').replace('/','').replace('=','')
cm = cm.replace('.',' ')

tokens = cm.split(' ')
tokens = filter(None,tokens)
cm = ' '.join(tokens)
cm = cm.replace('\n',' ')
tokens = cm.split(' ')
com=[]
for t in tokens:
    if not t in stop_words:
        com.append(t)
k = open('data/test.txt','w')


file = open('data/Comments.txt', 'r')
cm = file.readlines()

for i in range(0,10):
    st = cm[i]

    st = st.replace('.',' ')
    st = st.replace('"', '').replace('*', '').replace(';', '').replace('!', '').replace(':','').replace(')', '').replace('(', '').replace('?', '').replace('?', '').replace('_', '').replace('/', '').replace('=', '')
    tokens = st.split(' ')
    tokens = filter(None, tokens)

    comment = []
    for t in tokens:
        if not t in stop_words:
            comment.append(t)

    tfidf = 0

    for c in comment:

        tf = comment.count(c) / len(comment)
        
        idf = math.log(len(com) / com.count(c)) if com.count(c)!=0 else 0

        tfidf = tfidf + (tf*idf)

    tfidf = tfidf / len(comment)
    print tfidf
    #f = open('tf.txt','a')
    #f.write(str(tfidf) + '\n')


