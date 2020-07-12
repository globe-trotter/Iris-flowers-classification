import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.offline as pyo
import cufflinks as cf
from sklearn.preprocessing import LabelEncoder
cf.go_offline()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

iris = pd.read_csv("W:\Iris\Iris.csv")
iris.drop('Id',axis=1,inplace=True)
iris.rename(columns={'SepalLengthCm':'SepalLength','SepalWidthCm':'SepalWidth','PetalWidthCm':'PetalWidth','PetalLengthCm':'PetalLength'},inplace=True)
#sctr=px.scatter_matrix(iris,color='Species',dimensions=['SepalLength','SepalWidth','PetalWidth','PetalLength'])
#sctr.show()
label=iris['Species']
features=iris.drop(['Species'],axis=1)
#print(features.head())
encoder=LabelEncoder()
label=encoder.fit_transform(label)
#print(label)
features=np.array(features)

#splitting data for training and testing

features_train,features_test,label_train,label_test=train_test_split(features,label,test_size=0.3,random_state=0)

#decision_tree
DT=tree.DecisionTreeClassifier()
DT.fit(features_train,label_train)
prediction=DT.predict(features_test)
accuracy=accuracy_score(label_test,prediction)*100
# print(accuracy)
category=['Iris-Setosa','Iris-Versicolor','Iris-Virginica']

def findSpecies(sl,sw,pl,pw):
    feature=np.array([[sl,sw,pl,pw]])
    result=DT.predict(feature)
    print(category[int(result[0])])

sl=int(input("Enter sepal length in cm: "))
sw=int(input("Enter sepal width in cm: "))
pl=int(input("Enter petal length in cm: "))
pw=int(input("Enter petal width in cm: "))
findSpecies(sl,sw,pl,pw)