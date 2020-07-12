import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.offline as pyo
import cufflinks as cf
cf.go_offline()
iris = pd.read_csv("W:\Iris\Iris.csv")
iris.drop('Id',axis=1,inplace=True)
iris.rename(columns={'SepalLengthCm':'SepalLength','SepalWidthCm':'SepalWidth','PetalWidthCm':'PetalWidth','PetalLengthCm':'PetalLength'},inplace=True)
sctr=px.scatter_matrix(iris,color='Species',dimensions=['SepalLength','SepalWidth','PetalWidth','PetalLength'])
sctr.show()