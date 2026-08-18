import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, matthews_corrcoef

df=pd.read_csv("Telco-Customer-Churn.csv")
df.drop("customerID",axis=1,inplace=True)
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce")
df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].median())
df["Churn"]=df["Churn"].map({"No":0,"Yes":1})
cat_cols=df.select_dtypes(include=["object"]).columns
df=pd.get_dummies(df,columns=cat_cols,drop_first=True)
X=df.drop("Churn",axis=1)
y=df["Churn"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
models={"Logistic Regression":LogisticRegression(max_iter=2000),"Decision Tree":DecisionTreeClassifier(random_state=42),"KNN":KNeighborsClassifier(5),"Naive Bayes":GaussianNB(),"Random Forest":RandomForestClassifier(n_estimators=200,random_state=42),"SVM":SVC(probability=True)}
results=[]
for name,model in models.items():
    if name in ["Logistic Regression","KNN","SVM"]:
        model.fit(X_train_scaled,y_train)
        pred=model.predict(X_test_scaled)
        prob=model.predict_proba(X_test_scaled)[:,1]
    else:
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        prob=model.predict_proba(X_test)[:,1]
    results.append([name,accuracy_score(y_test,pred),roc_auc_score(y_test,prob),precision_score(y_test,pred),recall_score(y_test,pred),f1_score(y_test,pred),matthews_corrcoef(y_test,pred)])
print(pd.DataFrame(results,columns=["Model","Accuracy","AUC","Precision","Recall","F1 Score","MCC"]))