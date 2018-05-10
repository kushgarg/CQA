import RAKE
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
'''
rq = Rake()
rc = Rake()

rq.extract_keywords_from_text(question)
rc.extract_keywords_from_text(comment)

filet.write(str(rc.get_ranked_phrases_with_scores()))
'''

text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types."

rake = RAKE.Rake(RAKE.SmartStopList())
filet.write(str(rake.run(text,minCharacters=3,maxWords=5)).encode('utf-8'))