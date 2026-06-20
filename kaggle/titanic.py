import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('input/titanic/train.csv')
test = pd.read_csv('input/titanic/test.csv')

train.head()

train.info()