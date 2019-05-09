
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the DataSet
dataset=pd.read_csv('Data.csv')#read the data from csv file using panda
X=dataset.iloc[:, :-1].values #select a row and coloum from datasheet (-1)is total number of coloum -1 
y=dataset.iloc[:, 3].values 

#Taking Care of Missing Data
from sklearn.preprocessing import Imputer #Imputer is function of sklearn.preprocessing it is care of missing data from datasheet 
imputer=Imputer(missing_values='NaN',strategy='mean', axis=0)#axis is used for selecting rows or coloums 0 is for coloum and 1 for rows
imputer=imputer.fit(X[:, 1:3])#fit variable put a missing data  in data sheet
X[:, 1:3]=imputer.transform(X[:, 1:3])#replace missing data in matrix X

#Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()#Labelencoder encodes the mention data 
X[: , 0] = labelencoder_X.fit_transform(X[: , 0])#encode a index 0 of coloum
onehotencoder = OneHotEncoder(categorical_features =[0])#onehotencoder is encode a data on dummy variable
X = onehotencoder.fit_transform(X).toarray()#it is fit and transform a encode data 
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
