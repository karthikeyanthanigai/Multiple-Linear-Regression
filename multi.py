
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('insurance.csv')
#this function will provide the descriptive statistics of the dataset.(only int value)
dataset.describe()

#There are 4 independent variables and 1 dependent variable. So we need to see what is needed most importantly using the Correlation Matrix.
import seaborn as sns
#Other methods like Back Propagation/ Forward Propagation can be used. But Correlation Matrix is best for most speedy analysis.
correlation_matrix = dataset.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True)


#determine X and y variables(form correlation matrix we take age and bmi and we take gender,smokering values as independent variables)
X = dataset.iloc[:, [0,1,2,4]].values
y = dataset.iloc[:, [-1]].values

#label encoding for character data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
labelencoder1 = LabelEncoder()
X[:, -1] = labelencoder1.fit_transform(X[:, -1])

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

#split
from sklearn.model_selection import train_test_split
X_train ,X_test, y_train ,y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

#SGD
from sklearn.linear_model import SGDRegressor, LinearRegression
regressor = SGDRegressor(max_iter=10000, tol=1e-3, alpha =0.01, random_state = 0, learning_rate = 'invscaling' , eta0 = 0.0001)
regressor.fit(X_train, y_train)

#predicting the value
y_pred = regressor.predict(X_test)

#r2 result
from sklearn.metrics import r2_score, mean_squared_error
r_squared = r2_score(y_test, y_pred)
print("Coefficient of Determination = ",r_squared)


#rmse and r2 results for training set
from sklearn.metrics import r2_score , mean_squared_error

rmse_train = (np.sqrt(mean_squared_error(y_train, regressor.predict(X_train) )))
r_squared_train = r2_score(y_train , regressor.predict(X_train))
print("R squared for the training set")
print("---------------------------------")
print(r_squared_train)
print("---------------------------------")
print("RMSEfor the training set")
print("---------------------------------")
print(rmse_train)

#rmse and r2 results for test set
rmse_test = (np.sqrt(mean_squared_error(y_test, regressor.predict(X_test) )))
r_squared_test = r2_score(y_test , regressor.predict(X_test))
print("R squared for the testing set")
print("---------------------------------")
print(r_squared_test)
print("---------------------------------")
print("RMSEfor the testing set")
print("---------------------------------")
print(rmse_test)

#The RMSE and the R squared for the test and the training set is almost the same , which shows that our model has not done any overfitting. The model can be well improved by going to more Algorithms like Polynomial, SVMs , foresting and Boosting Algorithms.