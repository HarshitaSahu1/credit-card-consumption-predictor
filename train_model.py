import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import sys
print(sys.executable)

credit_consumption_data = pd.read_excel(r'C:\Users\Harshita Sahu\OneDrive\Documents\ML_1_CREDIT_CARD\11. Capstone Case Study - Predict Cred Card Consumption\CreditConsumptionData.xlsx')
credit_behaviour_data = pd.read_excel(r'C:\Users\Harshita Sahu\OneDrive\Documents\ML_1_CREDIT_CARD\11. Capstone Case Study - Predict Cred Card Consumption\CustomerBehaviorData.xlsx')
credit_demographics = pd.read_excel(r'C:\Users\Harshita Sahu\OneDrive\Documents\ML_1_CREDIT_CARD\11. Capstone Case Study - Predict Cred Card Consumption\CustomerDemographics.xlsx')

credit_consumption_data.head()
credit_behaviour_data.head()
credit_demographics.head()

#### To get the shape of the dataframes

credit_consumption_data.shape
credit_behaviour_data.shape
credit_demographics.shape

### To see If there are any duplicate values in the dataframes

credit_consumption_data['ID'].duplicated().sum()
credit_behaviour_data['ID'].duplicated().sum()
credit_demographics['ID'].duplicated().sum()

### To see if there are any null values in the dataframes

credit_consumption_data.isna().sum()
credit_behaviour_data.isna().sum()
credit_demographics.isna().sum()

cd_cb = credit_demographics.merge(credit_behaviour_data , on = 'ID',how = 'left')
cd_cb = cd_cb.merge(credit_consumption_data, on = 'ID', how = 'left')

cd_cb.to_csv('final_dataset.csv',index = False)

X_ = cd_cb.drop(['ID'],axis = 1)

X_train = X_[X_['cc_cons'].notna()]

X_test = X_[X_['cc_cons'].isna()] 

### to see if there is any outliers in the dataframes

X_train.describe(percentiles = [0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99])

### X_train has outliers 

X_train.info()

## here this is not having id column 

#credit_behaviour_data_updated = credit_behaviour_data.iloc[:,1:]

numeric_cols =[]
categorical_cols = []
for i in X_train.columns:
    if X_train[i].dtype == 'int64' or X_train[i].dtype == 'float64':
        numerics  = X_train[i]
        numeric_cols.append(i)
        plt.figure(figsize= (10,5))
        plt.boxplot(X_train[i].dropna())
        plt.title(f'Boxplot{numerics}')
        #plt.show()
        

    else:
        categorical_cols.append(i)


X = X_train.drop(['cc_cons'],axis = 1)
Y = X_train['cc_cons']

from sklearn.model_selection import train_test_split

X_t,X_v,Y_t,Y_v = train_test_split(X,Y,test_size = 0.2,random_state = 42)

X_t.shape
Y_t.shape
X_v.shape
Y_v.shape



from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import root_mean_squared_error,r2_score
import joblib

### split data into numeric & cat 
numeric_cols = X_t.select_dtypes(include = ['int64','float64']).columns.tolist()
categorical_cols = X_t.select_dtypes(include = ['object']).columns.tolist()

### piplines 

numeric_pipeline = Pipeline([('imputer',SimpleImputer(strategy= 'median')),('scaler',StandardScaler())])
categorical_pipeline = Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('one_hot_encoder',OneHotEncoder(handle_unknown= 'ignore',drop = 'first'))])

### Column Transfomers 

processors = ColumnTransformer(transformers=[('num',numeric_pipeline,numeric_cols),('cat',categorical_pipeline,categorical_cols)])

model = Pipeline([("processors",processors),
                  
                  ('model',BaggingRegressor(estimator= DecisionTreeRegressor(random_state=101),n_estimators= 20,random_state = 101))])


model.fit(X_t,Y_t)

joblib.dump(model,'model_pipeline.pkl')



pred = model.predict(X_v)

print('predicted !')

print(f'rmse score training prediction', root_mean_squared_error(Y_v,pred))
print(f'r2_score score training prediction', r2_score(Y_v,pred))
print('completed !')

X_test.iloc[:,-1:] = model.predict(X_test)

X_test