import pandas as pd
df=pd.read_csv("apple_quality.csv")

#null remove
print(df.isnull().sum())
df=df.dropna()
print(df.isnull().sum())

#drop colum
df=df.drop(['A_id'],axis=1)

#Label encoding
category_colums=['Quality']
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df[category_colums] = df[category_colums].apply(encoder.fit_transform)

#data type
print(df.dtypes)
df.Acidity=df.Acidity.astype('float')
print(df.dtypes)

#data label 
X=df.iloc[:,:7]
y=df.iloc[:,7]

#array convert
X=X.to_numpy()
y=y.to_numpy()

#split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

#ML train
from sklearn.svm import SVC
model=SVC()
model.fit(X_train,y_train)

#ML test
y_pred=model.predict(X_test)

#parameters
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
import pickle
pickle.dump(model,open("Apple.pkl","wb"))

