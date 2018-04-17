from pyjarowinkler import distance
import ngram
import jellyfish
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words.remove("no")

import xlwt

def lcs(X, Y):
    # Find lengths of two strings
    m = len(X)
    n = len(Y)

    L = [[0 for i in range(n + 1)] for j in range(2)]

    # Binary index, used to index current row and
    # previous row.
    bi = bool

    for i in range(m):
        # Compute current binary index
        bi = i & 1

        for j in range(n + 1):
            if i == 0 or j == 0:
                L[bi][j] = 0

            elif X[i] == Y[j - 1]:
                L[bi][j] = L[1 - bi][j - 1] + 1

            else:
                L[bi][j] = max(L[1 - bi][j], L[bi][j - 1])

    # Last filled entry contains length of LCS
    # for X[0..n-1] and Y[0..m-1]
    return L[bi][n]


import re, math
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def jaccard(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


fh = open('data/GOLD_RelevantQues.txt', 'r')
rq = fh.readlines()
fh = open('data/GOLD_Comments.txt', 'r')
cm = fh.readlines()
fh = open('data/GOLD_Labels.txt', 'r')
lb = fh.readlines()

f = open('data/GOLD_output.txt','w')
str2 = ""

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("LABELS_2")

sheet.write(0,0,"LCS")
sheet.write(0,1,"Cosine-Similarity")
sheet.write(0,2,"Jaccard-Index")
sheet.write(0,3,"Jaro-Winkler")
sheet.write(0,4,"Damareu-Levenshtein")
sheet.write(0,5,"NGram")
sheet.write(0,6,"class")

for i in range(0, 327):
    for j in range(0, 10):
        k = j + i * 10

        req = ""
        com = ""

        for r in rq[i].split():
            if not r in stop_words:
                req = req + r + " "

        req = req.replace('"', '').replace('*', '').replace(';', '').replace('!','').replace(':','').replace(')','').replace('(','').replace('?','').replace('-','').replace('_','').replace('/','').replace('=','')

        if k != 476 and k != 2548:
            for r in cm[k].split():
                if not r in stop_words:
                    com = com + r + " "
        else:
            com = cm[k]

        com = com.replace('"', '').replace('*', '').replace(';', '').replace('!','').replace(':','').replace(')','').replace('(','').replace('?','').replace('-','').replace('_','').replace('/','').replace('=','')

        print str(k) + '\n'
        print req + '\n' + com + '\n'

        if com != "":
            vector1 = text_to_vector(req)
            vector2 = text_to_vector(com)

            list1 = req.split()
            list2 = com.split()
            words1 = set(list1)
            words2 = set(list2)

            lcs1 = str(lcs(req, com))
            cos = str(get_cosine(vector1, vector2))
            ji = str(jaccard(words1,words2))
            jw = str(distance.get_jaro_distance(req,com , winkler=True, scaling=0.1))
            dl = str(jellyfish.damerau_levenshtein_distance(unicode(req,'utf-8'),unicode(com,'utf-8')))
            ng = str(ngram.NGram.compare(req,com))
        else:
            lcs1 = cos = ji = jw = dl = ng = 0.0

        str2 = str2 + " " + rq[i] + " " + cm[k] + " LCS :" + lcs1 + " Cosine :" + cos + " Jaccard index:" + ji + " Jaro-winkler:"+ jw + " Damerau-Levenshtein:"+ dl + " NGram: " + ng + " RELEVANCE : " + lb[k] + '\n' +  '\n'

        sheet.write(k + 1, 0,lcs1)
        sheet.write(k + 1, 1, cos)
        sheet.write(k + 1, 2, ji)
        sheet.write(k + 1, 3, jw)
        sheet.write(k + 1, 4, dl)
        sheet.write(k + 1, 5, ng)
        sheet.write(k + 1, 6, lb[k].replace('\n',''))

book.save("data/GOLD_trial.xls")
f.write(str2)
f.close()







