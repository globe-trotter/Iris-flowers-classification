import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.offline as pyo
import cufflinks as cf
cf.go_offline()
iris = pd.read_csv("W:\Iris\Iris.csv")
iris.drop('Id',axis=1,inplace=True)
print(iris.head())