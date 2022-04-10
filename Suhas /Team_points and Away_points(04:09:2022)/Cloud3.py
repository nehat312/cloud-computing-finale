#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
#%%
df = pd.read_csv('/Users/suhasburavalla/Desktop/Dataset.csv' )

#%%
cols = ['gmDate', 'gmTime', 'seasTyp', 'teamAbbr','teamPTS', 'teamAST', 'teamTO', 'teamSTL', 'teamBLK', 'teamPF', 'teamFG%', 'team3P%', 'teamFT%', 'teamTRB','teamRslt', 'teamOrtg', 'teamDrtg',  'opptAbbr', 'opptPTS', 'opptAST', 'opptTO', 'opptSTL', 'opptBLK', 'opptPF', 'opptFG%', 'oppt3P%', 'opptFT%', 'opptTRB', 'opptOrtg', 'opptDrtg']

# %%
dfnew = df[cols]
#%%
df1 = dfnew[dfnew.index % 2 == 0]  # Excludes every other row 
#%%
df1 = df1.rename(columns={"teamFG%": "teamFG", "team3P%": "team3P", "teamFT%" : "teamFT","opptFG%": "opptFG", "oppt3P%": "oppt3P", "opptFT%" : "opptFT" })
#%%
#%%
X = df1[['teamAST', 'teamTO', 'opptAST', 'opptTO', 'teamDrtg', 'teamOrtg', 'opptDrtg', 'opptOrtg', 'teamFG', 'opptFG', 'teamTRB', 'opptTRB']]
y = df1['opptPTS']
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#%%
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#%%
y_pred = regressor.predict(X_test)

#%%
print(y_pred)

#%%
resultPTS = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
resultPTS

#%%
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


#%%
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

#%%
coefficients = regressor.coef_

intercept = regressor.intercept_
# %%
def calculate_OpptPTS(ASTteam, TOteam, ASToppt, TOoppt, Drtgteam, Ortgteam, Drtgoppt, Ortgoppt, FGteam, FGoppt, TRBteam, TRBoppt ):
  return (ASTteam * coefficients[0]) + ( TOteam * coefficients[1]) + ( ASToppt* coefficients[2]) + ( TOoppt* coefficients[3])+ + ( Drtgteam* coefficients[4])+ ( Ortgteam* coefficients[5])+ ( Drtgoppt* coefficients[6])+  ( Ortgoppt* coefficients[7])+ ( FGteam * coefficients[8]) + ( FGoppt * coefficients[9]) + ( TRBteam * coefficients[10]) + ( TRBoppt * coefficients[11]) + intercept



