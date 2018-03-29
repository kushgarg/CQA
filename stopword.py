
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
file1 = open("data/Comments.txt")
line = file1.readlines()


file2 = open('data/filteredtext.txt','w')
str1 = ""

for r in line[0].split():
    if not r in stop_words:
        str1 = str1 + r + " "

file2.write(str1)
file2.close()
