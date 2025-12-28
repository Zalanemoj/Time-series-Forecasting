import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv('Client1')

test_size=.2
split_idx = int(len(df) * (1 - test_size))

train=df.iloc[:split_idx]
test=df.iloc[split_idx:]

train.to_csv('Train')
test.to_csv('test')