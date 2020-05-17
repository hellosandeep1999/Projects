# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:18:18 2020

@author: user
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


housing = pd.read_csv("data.csv")


#Data Exploring

housing.head()
housing.info()  #all row are complete

housing['CHAS'].value_counts()  #it will give count value


housing.isnull().any(axis=0)  #cheking missing value
housing.describe()        #housing data description
housing['RM'].describe()     #checking that how many values null in RM column

housing.hist(bins=50, figsize=(20, 15))    




"""
here we need to deivide our dataset into two parts one in train dataset
and second is test dataset because it is better for when our model is ready for testing.

#for learning purpose
def split_train_test(data, test_ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    print(shuffled)
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[train_indices]

train_set, test_set = split_train_test(housing, 0.2)
"""

from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(f'Row in train set {len(train_set)} \nRow of test set {len(test_set)}')


"""


"""


from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits =1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
     strat_train_set = housing.loc[train_index]
     strat_test_set = housing.loc[test_index]



#some extra Exploration
strat_train_set['CHAS'].value_counts()  #376/28  =  13.42 
strat_test_set['CHAS'].value_counts()   #95/7    = 13.57

housing = strat_train_set.copy()

#Now we will looking for correlation between "MEDV" and other features and labels
# 1 - strong Positive Correlation

corr_matrix = housing.corr()
corr_matrix["MEDV"].sort_values(ascending = False)


#So we will check by some of most important graph like between strong
#positive and strong negaitve graph

from pandas.plotting import scatter_matrix
attributes = ["MEDV","RM","ZN","LSTAT"]
scatter_matrix(housing[attributes],figsize=(12,8))


"""
we will check graph here see that diagonal value show how many values
and one of the most important good graph we can see

                MEDV  ---->   LSTAT   (vice-versa)
                RM    ---->   MEDV    (vice-versa)
                
"""





housing.plot(kind="scatter",  x="RM",  y="MEDV", alpha=0.8)

housing["TAXRM"] = housing['TAX']/housing['RM']

housing.head()


corr_matrix = housing.corr()
corr_matrix["MEDV"].sort_values(ascending = False)

housing.plot(kind="scatter",  x="TAXRM",  y="MEDV", alpha=0.8)



housing = strat_train_set.drop("MEDV", axis = 1)
housing_labels = strat_train_set["MEDV"].copy()  


"""
#Now we will do work on missing values
To take care of missing attributes, you have three options:
    1. Get rid of the missing data points
    
       
    
    2. Get rid of the whole attribute
    
       
       
    3. Get the value to some value (0, mean or median)
    
       
"""
a = housing.dropna(subset = ["RM"]) #option - 1
a.shape
#Note there is no row which contains nan value but orginal data is safe      
       
housing.drop('RM',axis=1).shape  #option - 2
#Note there is no RM column and also note that the original housing dataframe


median = housing["RM"].median()   #option - 3
housing["RM"].fillna(median)
# Note that the original housing dataframe will remain unchanged


from sklearn.impute import SimpleImputer       #may be in test_set have null value in RM column
imputer = SimpleImputer(strategy = "median")
imputer.fit(housing)

imputer.statistics_.shape

X = imputer.transform(housing)
housing_tr = pd.DataFrame(X, columns=housing.columns)

housing_tr.describe()


"""
#Scikit-learn 
Primarily, three types of objects
1. Estimators - It estimates some parameter based on a dataset. Eg. imputer It 
has a fit method and transform method fit method - Fits the dataset and 
calculates internal parameters

2. Transformer - transform method takes input and returns output based on the
learning from fit(). It also has a convenience function called fit_transform()
which fits and then transforms. 

3. Predictors  - LinearRegrssion model is an example of predictors. fit() and 
predict() are two common function. It also gives score function which will
evaluates the prediction.
"""


"""
#Feature Scaling
Primarily, two types of feature scaling methods:
    1. Min-Max scaling (Normalization)
      (value - min)/(max-min)
      Sklearn provides a class called MinMaxScaler for this
      
    2.Standartization
      (Value - mean)/std
      Sklearn provides a class called Standard Scaler for this
      

"""


#Creating a Pipeline(for easily changeg)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy = 'median')),
        #   ....  add as many as you want in your pipeline
        ('std_scaler', StandardScaler()),
])

    
housing_num_tr = my_pipeline.fit_transform(housing)
housing_num_tr.shape


#Selecting a desired model for Real Estates
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
#model = LinearRegression()
#model = DecisionTreeRegressor()
model = RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)

#now we will take some data

some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]

prepared_data = my_pipeline.transform(some_data)

model.predict(prepared_data)

print(list(some_labels))


#Evaluating the model
from sklearn.metrics import mean_squared_error
housing_predictions = model.predict(housing_num_tr)
lin_mse = mean_squared_error(housing_labels,housing_predictions)

lin_rmse = np.sqrt(lin_mse)

print(lin_rmse)

#when we are using decisiontreeregressor then our model is making overfitting

#Using better evaluation technique - Cross Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, housing_num_tr,housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)

print(rmse_scores)

def print_scores(scores):
    print("Scores:", scores)
    print("Mean: ", scores.mean())
    print("Standard deviation: ", scores.std())
    

print_scores(rmse_scores)


#saving the model
from joblib import dump, load
dump(model, 'housingRealstate.joblib')


#testing the model on test data
X_test = strat_test_set.drop("MEDV", axis=1)
Y_test = strat_test_set["MEDV"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_predictions = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test,final_predictions)
final_rmse = np.sqrt(final_mse)

print(final_rmse)













