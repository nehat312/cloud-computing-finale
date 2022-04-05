import pandas as pd

df = pd.read_csv('data/tr_data_hub_3-30-22.csv')
df.set_index("Team", inplace=True)
pairs = [
    ['Charlotte', 'Orlando'],
    ['Toronto', 'Philadelphia'],
    ['Milwaukee','Boston'],
    ['Minnesota', 'San Antonio'],
    ['New Orleans', 'Portland'],
    ['Denver', 'Memphis'],
    ['Golden State', 'Los Angeles']]

def new_row(pair, df):
    x = pair[0].lower()
    y = pair[1].lower()
    x_row = df.loc[x]
    y_row = df.loc[y]
    diff = pd.DataFrame()
    diff['Home'] = x
    diff['Away'] = y
    row_subtract = x_row-y_row
    frame = row_subtract.to_frame().T
    #list = [diff,row_subtract]
    #final_df = pd.concat(list, axis=1)
    return frame
#%%
pair = pairs[0]
x = pair[0].lower()
y = pair[1].lower()
x_row = df.loc[x]
y_row = df.loc[y]
diff = pd.DataFrame()
diff['Home'] = x
diff['Away'] = y
row_subtract = x_row-y_row
frame = row_subtract.to_frame().T
t = new_row(pairs[1],df)
#%%
test_list = []
for x in range(0,len(pairs)-1):
    test_list.append(new_row(pairs[x], df))
#%%
df_finale = pd.DataFrame()
df_finale['Home'] = [x[0] for x in pairs]
df_finale['Away'] = [x[1] for x in pairs]
#df_finale.to_csv('finale.csv')
#%%
test_list = [df_finale]
f_list =[test_list.append(new_row(pairs[x], df)) for x in range(len(pairs))]
#%%
df_diff = pd.concat(f_list, axis=0)
#%%
#df_diff.to_csv('test.csv')

