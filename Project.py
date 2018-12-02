
# coding: utf-8

# In[8]:


import csv
txt_file=r"SemEval2018-T3-train-taskA_emoji_ironyHashtags.txt"
csv_file=r"data1.csv"
in_txt= csv.reader(open(txt_file,'r',errors='ignore'),delimiter='\t')
out_csv=csv.writer(open(csv_file,'w'))
out_csv.writerows(in_txt)


# In[22]:


import emoji
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
with open('data1.csv')as csvfile:
    de_emojize=emoji.demojize(csvfile.read())
    commonurl_str = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'http://someurl', de_emojize)
    replace_username=re.sub('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)','@someuser',commonurl_str)
    input_txt=replace_username+'\n'
print(input_txt)
input_tokenized=nltk.word_tokenize(input_txt)
#print(input_tokenized)
input_posTag=nltk.pos_tag(input_tokenized)
print(input_posTag)

