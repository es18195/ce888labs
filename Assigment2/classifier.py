#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:36:27 2019

@author: EduSune
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cPickle

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import accuracy_score as acc
from sklearn.metrics import make_scorer
from sklearn.dummy import DummyRegressor
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import LabelEncoder


f = open("./data.txt")
contents = f.read()
df = contents.replace('[','').replace(']','')
file = open('newdata.txt', 'w')
file.write(df)
file.close()
df = pd.read_csv("./newdata.txt", delimiter = ",")
y_df=df.values[:,9]
x_df= np.delete(df.values, 9, 1)
print(x_df)

from sklearn.ensemble import GradientBoostingClassifier


clf = GradientBoostingClassifier(n_estimators = 2000,max_depth = 4,warm_start=True)
clf.fit(x_df,y_df)

print(acc(y_df,clf.predict(x_df)))

# save the classifier
with open('classifierOG.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)    
