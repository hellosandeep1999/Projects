# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:59:09 2020

@author: user
"""

#Mathod 1

import pandas as pd

rawdata = open("SMSSpamCollection").read()
#rawdata[0:500]

parsed_data = rawdata.replace("\t","\n").split("\n")

label = parsed_data[0::2]
msg_data = parsed_data[1::2]

len(label)
len(msg_data)

label = label[:-1]

combine_data = pd.DataFrame({"label":label,"msg":msg_data})


#we can head 5 rows
combine_data.head()

------------------------------------------------------------------------------------

#Mathod 2

dataset = pd.read_csv("SMSSpamCollection",sep='\t',header=None)

#it will maximum column
pd.set_option("display.max_colwidth",100)

#Now we will do the explore data with some of basic commands
#1 How may rows
#2 How many ham/spam
#3 How many missing data


dataset.head()  #some head rows
dataset.columns = ["label","sms"]  #giving the column names

#shape of data
print(f'{len(dataset)},{len(dataset.columns)}')
dataset.shape

#number of ham and spam
print(f'ham={len(dataset[dataset["label"] == "ham"])}')
print(f'spam={len(dataset[dataset["label"] == "spam"])}')

#missing data
print(f'number of missing label={dataset["label"].isnull().sum()}')




"""
Text preprocessing
1 remove punctualation 
2 tokenization
3 remove stop words
4 stemming / lemmatizing

"""


#Removing punctualization

import string

string.punctuation  #to all punctuation

def remove_punctuation(txt):
    txt_amount = "".join([c for c in txt if c not in string.punctuation])
    return txt_amount

dataset['msg_clean'] = dataset["sms"].apply(lambda x: remove_punctuation(x))

dataset.head()



#Tokenization

import re
def tokenize(txt):
    tokens = re.split("\W+",txt)
    return tokens
dataset['msg_clean_tokenized'] = dataset['msg_clean'].apply(lambda x : tokenize(x.lower()))



#Removing stop words
import nltk
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')

stop_words[:10]


def remove_stopwords(txt_tokenized):
    txt_clean = [word for word in txt_tokenized if word not in stop_words]
    return txt_clean

dataset["msg_no_stop_words"] = dataset['msg_clean_tokenized'].apply(lambda x : remove_stopwords(x))

dataset.head()

























