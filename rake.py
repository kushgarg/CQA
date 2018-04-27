from rake_nltk import Rake
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


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
#cm = cm.replace('\n',' ')
#tokens = cm.split(' ')

ques = ' '.join(tokens1)
#ques = ques.replace('\n',' ')
#tokens1 = ques.split(' ')


com=[]
for t in tokens:
    if not t in stop_words:
        com.append(t)

qt=[]
for t in tokens1:
    if not t in stop_words:
        qt.append(t)

comment = ' '.join(com)
question = ' '.join(qt)

filet = open('data/test.txt','w')

rq = Rake()
rc = Rake()

rq.extract_keywords_from_text(question)
rc.extract_keywords_from_text(comment)

filet.write(str(rc.get_ranked_phrases_with_scores()))