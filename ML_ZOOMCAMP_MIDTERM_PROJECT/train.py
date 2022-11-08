import numpy as np #numerical operations
import pandas as pd #for EDA
import seaborn as sns #data visualization
import matplotlib.pyplot as plt #data visualization
import warnings
warnings.filterwarnings("ignore") 
from datetime import timedelta
import re
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import xgboost as xgb



data = pd.read_csv("solar.csv")

data.columns = data.columns.str.replace(' ','-') # replacing space between words with underscore

for i in ['Path-Width-(km)','Central-Duration']:
    data[i].fillna('0',inplace=True)

def Eclipse(x):  #4 types of lunar eclipse mentioned at the starting: P, A, T, H 
    if 'P' in x:
        return('P')
    if 'A' in x:
        return('A')
    if 'T' in x:
        return('T')
    if 'H' in x:
        return('H')


data['Eclipse-Type'] = list(map(Eclipse,data['Eclipse-Type']))


def cleaningdate(x):     
    if '-' in x:
        x = x.replace('-','')
    return x


data['Calendar-Date'] = list(map(cleaningdate, data['Calendar-Date'])) 

calendar_date = data['Calendar-Date'].str.split(' ')

data['Calendar-Year'] = calendar_date.str[0]
data['Calendar-Month'] = calendar_date.str[1]
data['Calendar-Day'] = calendar_date.str[2].astype(float)


def change_into_datetime(col):
    data[col] = pd.to_datetime(data[col])


for i in ['Eclipse-Time']:
    change_into_datetime(i)


def extract_hour(df,col):
    data[col + '-hour'] = data[col].dt.hour
  
def extract_minute(df,col):
    data[col + '-minute'] = data[col].dt.minute

def extract_seconds(df,col):
    data[col + '-seconds'] = data[col].dt.second


extract_hour(data,'Eclipse-Time')
extract_minute(data,'Eclipse-Time')
extract_seconds(data,'Eclipse-Time')


data.drop(['Eclipse-Time'],axis=1,inplace=True)


data.drop(['Calendar-Date','Catalog-Number'],axis=1,inplace=True)


data['Latitude-number'] = data['Latitude'].str.slice(stop=-1)
data["Latitude-number"] = pd.to_numeric(data["Latitude-number"])
data['Latitude-letter'] = data['Latitude'].str.slice(start=-1)


data['Longitude-number'] = data['Longitude'].str.slice(stop=-1)
data["Longitude-number"] = pd.to_numeric(data["Longitude-number"])
data['Longitude-letter'] = data['Longitude'].str.slice(start=-1)


data.drop(['Latitude','Longitude'],axis=1,inplace=True)


data['Duration-minutes'] = data['Central-Duration'].str.slice(stop=2)
data['Duration-seconds'] = data['Central-Duration'].str.slice(start=3,stop=-1)
data.drop(['Central-Duration'],axis=1,inplace=True)


lat = pd.get_dummies(data['Latitude-letter'])
lon = pd.get_dummies(data['Longitude-letter'])

data = pd.concat([data,lat,lon],axis=1)

data.drop(['Latitude-letter','Longitude-letter'],axis=1,inplace=True)


label = LabelEncoder()

for i in ['Calendar-Month']:
    data[i] = label.fit_transform(data[i])


data['Path-Width-(km)'] = list(map(cleaningdate, data['Path-Width-(km)'])) 
data['Duration-minutes'] = list(map(cleaningdate, data['Duration-minutes']))
data['Duration-seconds'] = list(map(cleaningdate, data['Duration-seconds']))

data["Path-Width-(km)"] = pd.to_numeric(data["Path-Width-(km)"])
data["Duration-minutes"] = pd.to_numeric(data["Duration-minutes"])
data["Duration-seconds"] = pd.to_numeric(data["Duration-seconds"])
data["Calendar-Year"] = pd.to_numeric(data["Calendar-Year"])


data = data.drop(['Duration-seconds'], axis = 1)
data = data.dropna(axis=0, subset=['Path-Width-(km)','Duration-minutes'])


X = data.drop('Eclipse-Type', axis=1)

data_extract = X.copy()




X = X.values
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)
X = pd.DataFrame(X_scaled)



transformer = Normalizer().fit(X)
X_normalized = transformer.transform(X)
pd.DataFrame(X_normalized)


y = data['Eclipse-Type']
le = LabelEncoder()  
y = le.fit_transform(y)


data_normalized = X_normalized.copy()



X_full_train, X_test, y_full_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=259)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=259)


#Using XGBoost

XGBclassifier = xgb.XGBClassifier(random_state=259)
XGBclassifier.fit(X_full_train, y_full_train)
y_pred = XGBclassifier.predict(X_test)



print("\nBelow is the classification report:\n")
print(classification_report(y_test,y_pred))
print("Below is the test set accuracy:\n")
print(accuracy_score(y_test, y_pred))


from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print("\n")
print("And the confusion matrix is:\n")
print(confusion_matrix)


data_sample = data_extract.iloc[-3].values
print("\n")
print(data_sample)






