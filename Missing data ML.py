import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Data.csv')#read the data from csv file using panda
X=dataset.iloc[:, :-1].values #select a row and coloum from datasheet (-1)is total number of coloum -1 
y=dataset.iloc[:, 3].values 
from sklearn.preprocessing import Imputer #Imputer is function of sklearn.preprocessing it is care of missing data from datasheet 
imputer=Imputer(missing_values='NaN',strategy='mean', axis=0)#axis is used for selecting rows or coloums 0 is for coloum and 1 for rows
imputer=imputer.fit(X[:, 1:3])#fit variable put a missing data  in data sheet
X[:, 1:3]=imputer.transform(X[:, 1:3])#replace missing data in matrix X

#encoding Categorial data
from sklearn.preprocessing import LabelEnconder, OneHotEnconder#label encoder is encode a values 
labelenconder_X=LabelEncoder()
X[:, 0]=labelenconder_X.fit_transform(X[:, 0])#LabelEncoder fit a enconder value of Index value of 0 (X matrix index 0)Country coloum
onehotencoder=OneHotEncoder(categorical_feature = [0])#OneHotEncoder is used to classified in order

#onehotencoder=OneHotEncoder(categorical_feature = [0]) is used to select a X matrix which is Categorical and select a index number (0) of X

X = onehotencoder.fit_transform(X).toarray()
