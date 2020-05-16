# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:59:09 2020

@author: user
"""
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

-----------------------------------------------------------------------------------------------
"""



#Project Starts From Here




#Import all libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Data gathering and Data collection
dataset = pd.read_csv("SMSSpamCollection",sep='\t',header=None)

#it will maximum column
pd.set_option("display.max_colwidth",100)

#Now we will do the explore data with some of basic commands
#1 How may rows
#2 How many ham/spam
#3 How many missing data

dataset.head()  #some head rows

dataset.columns = ["label","sms"]  #giving the column names

#Now I want to two more column for length of massage and punctuation


#for lenght column
dataset['length'] = list(map(lambda x:len(x),dataset['sms']))


#for punctuation column
import string

string.punctuation  #to all punctuation

def remove_punctuation(txt):
    txt_amount = "".join([c for c in txt if c not in string.punctuation])
    return txt_amount

dataset['punc'] = list(map(lambda x,y:len(x)-len(y),dataset['sms'],
                                    dataset["sms"].apply(lambda x: remove_punctuation(x))))






#Now we will Explore the dataset


#shape of data
dataset.shape  #(5572, 4)
#print(f'{len(dataset)},{len(dataset.columns)}')


#number of ham and spam
print(f'ham={len(dataset[dataset["label"] == "ham"])}')    #length of ham == 4825
print(f'spam={len(dataset[dataset["label"] == "spam"])}')  #length of spam == 747


#missing data
print(f'number of missing label={dataset["label"].isnull().sum()}')    #missing value == 0

dataset['label'].value_counts()  # number of ham and spam massage 
dataset['label'].value_counts(normalize=True) 

dataset.index  #to check indexing
dataset.columns.tolist()  #name of all column names
dataset.dtypes  #all columns datatypes
dataset.values.tolist()


#Balence the data
ham = dataset[dataset['label'] == 'ham']   #For ham massage
ham.head()


spam = dataset[dataset['label'] == 'spam']    #For spam massage
spam.head()



#Now we will same lenght of ham and spam so first we will check the shape then we will do the conversion
ham.shape,spam.shape
ham = ham.sample(spam.shape[0])
ham.shape


#Now we will add all spam data in after ham
data = ham.append(spam, ignore_index=True)
data.head()
data.tail()




plt.hist(data[data['label'] == 'ham']['length'], bins = 100,alpha=0.8) #histogram for lenght off all ham and spam
plt.hist(data[data['label'] == 'spam']['length'],bins = 100,alpha=0.8)
plt.grid(axis='y')
#plt.ylim(ymax = 100)
plt.show()

plt.hist(data[data['label'] == 'ham']['punc'], bins = 100,alpha=0.8) #histogram for lenght off all ham and spam
plt.hist(data[data['label'] == 'spam']['punc'],bins=100,alpha=0.8)
plt.grid(axis='y')
#plt.ylim(ymax = 100)
plt.show()





#Data Preparation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

from sklearn.feature_extraction.text import TfidfVectorizer

x_train,x_test,y_train,y_test = train_test_split(data['sms'],data['label'],test_size=0.3,shuffle=True,stratify=data['label'])



#Bags of words
vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(x_train)
x_train.shape

clf = Pipeline([('tfidf',TfidfVectorizer()),('clf',RandomForestClassifier(n_estimators=100,n_jobs=-1))])

#this line give the error so here one thing we need to remember
#that when we use the pipepline then the data has been changes so we need 
#to run tarin_test_split(line no. 163)
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

confusion_matrix(y_test,y_pred)  #finding the confusion matrix for evaluation of model 

"""
array([[1446,    2],
       [  36,  188]], dtype=int64)
    
"""

print(classification_report(y_test,y_pred))

accuracy_score(y_test,y_pred)  #0.9487750556792873   It means we can say that it is a best accuracy 
                                                    #for prediction of our model for new data
                                                    
                                                    
#So now we will take some dummy massages for testing our model

"""
massage1 = "Hey Whatsapp!"
massage2 = "Congratulations! you get a Free ticket for summer"

"""
#testing -1
 
clf.predict(["Hey Whatsapp!"])    #array(['ham'], dtype=object)


#testing -2

clf.predict(["Congratulations!,free tickets to the USA this summer"])  #array(['spam'], dtype=object)



#this was all by the random forest algorithm








-----------------------------------------------------------------------------------------------



#now we will use the SVM algorithm


clf = Pipeline([('tfidf',TfidfVectorizer()),('clf',SVC(C = 1000 , gamma = 'auto'))])

clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

confusion_matrix(y_test,y_pred) #finding the confusion matrix for evaluation of model 

"""
array([[216,   8],
       [  9, 216]], dtype=int64)
    
    """
    
print(classification_report(y_test,y_pred))

accuracy_score(y_test,y_pred)  #0.9621380846325167   It means we can say that it is a best accuracy 
                                                    #for prediction of our model for new data
                                                    
                                                    
#So now we will take some dummy massages for testing our model

"""
massage1 = "Hey Whatsapp!"
massage2 = "Congratulations! you get a Free ticket for summer"

"""
#testing -1
 
clf.predict(["Hey Whatsapp!"])    #array(['ham'], dtype=object)


#testing -2

clf.predict(["Congratulations!,free tickets to the USA this summer"])   #array(['spam'], dtype=object)








------------------------------------------------------------------------------------------------------

+++++++++++++++++++++++++++++++++++++++++++++


#####################
#Final Result:
####################



"""
Here SVM algorithm is giving better accuracy. Random forest also giving best accuracy.
and now we can find the a massage ham or spam.
"""



++++++++++++++++++++++++++++++++++++++++++++++=































