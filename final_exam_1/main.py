import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('medical_examination.csv')

data = data.drop_duplicates()  
data = data.dropna() 