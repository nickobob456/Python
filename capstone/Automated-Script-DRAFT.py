import pandas as pd
import numpy as np
from scipy import stats

# import S&P500 price data 
df_sp500 = pd.read_csv('C:\\Users\\Nicholas\\Documents\\berkeley\\Capstone\\SP500.csv')

# import competitor price data
df_ibm = pd.read_csv('C:\\Users\\Nicholas\\Documents\\berkeley\\Capstone\\xerox.csv')

# reorder dataframes by dates
df_sp500 = df_sp500.sort_values(by = 'Date', ascending = 1).reset_index(drop = True)
df_ibm = df_ibm.sort_values(by = 'Date', ascending = 1).reset_index(drop = True)

# add new columns for % changes in adjusted closing prices
df_sp500['AdjChange'] = df_sp500['Adj Close'].pct_change()
df_ibm['AdjChange'] = df_ibm['Adj Close'].pct_change()
 

# define windows (we will pass issue date later as a variable)
df_issuedate_index = int(df_ibm.index[df_ibm['Date'] == '1998-12-15'].values)
df_eventwindow = df_ibm.iloc[df_issuedate_index - 3 :df_issuedate_index + 4,:]
df_estimationwindow = df_ibm.iloc[df_issuedate_index - 123 :df_issuedate_index - 3,:]
df_posteventwindow = df_ibm.iloc[df_issuedate_index + 4 :df_issuedate_index + 124,:]

df_eventwindow_sp500 = df_sp500.iloc[df_issuedate_index - 3 :df_issuedate_index + 4,:]
df_estimationwindow_sp500 = df_sp500.iloc[df_issuedate_index - 123 :df_issuedate_index - 3,:]
df_posteventwindow_sp500 = df_sp500.iloc[df_issuedate_index + 4 :df_issuedate_index + 124,:]


# APPEND POST EVENT WINDOW FOR ESTIMATION OF BETA
# regression for estimation window
x = pd.concat([df_estimationwindow['AdjChange'],df_posteventwindow['AdjChange']])
y = pd.concat([df_estimationwindow_sp500['AdjChange'],df_posteventwindow_sp500['AdjChange']])

slope, intercept, r_value, p_value, std_err = stats.linregress(y,x)


# calculate expected and abnormal returns 
expected_returns = slope * df_eventwindow_sp500['AdjChange'] + intercept
abnormal_returns = df_eventwindow['AdjChange'] - expected_returns 
cumulative_abnormal_returns = abnormal_returns.cumsum()

print (sum(cumulative_abnormal_returns))

