import pandas as pd
import numpy as np
import json
df = pd.read_csv('Results.csv')
dict_result = [{1:100}]
for z in range(len(df)):
    name_file = df.iloc[z]['Filename']
    #print(name_file)
    file_name = "Challenge Dataset/"
    with open(file_name + name_file + '.txt', 'r') as file:
        x = file.read()
        y = x.split('\n')
        y = [x.split('  ') for x in y]
        #print(y)
        
    for j in range(len(y)):
        while(y[j].count('') != 0):
            y[j].remove('')
            
    head = [y[j] for j in range(len(y) - 1) if '£' in y[j+1] or ' £' in y[j+1] or '£ ' in y[j+1] or 'Â£' in y[j+1] or ' Â£ ' in y[j+1] or 'Â£ ' in y[j+1] or ' Â£' in y[j+1]]
    
    s = 0
    e = 0
    
    for i in range(len(y)):
        if '£' in y[i] or ' £' in y[i] or '£ ' in y[i] or 'Â£' in y[i] or ' Â£ ' in y[i] or 'Â£ ' in y[i] or ' Â£' in y[i]:
            s = i
    del y[s]
    
    for i in range(len(y)):
        if 'STATEMENTS' in y[i] or ' STATEMENTS' in y[i] or 'STATEMENTS ' in y[i] or ' STATEMENTS ' in y[i]:
            e = i
            
    for i in range(len(y)):
        if 'Capital and reserves' in y[i] or ' Capital and reserves' in y[i] or 'Capital and reserves ' in y[i] or ' Capital and reserves ' in y[i]:
            e = i+1
            
    y_new = y[s-1:e]
    
    try:
        head = head[0]
    except:
        pass
    try:
        mx = 0
        l= []
        for i in range(len(y_new)):
            l.append(len(y_new[i]))
        mx= max(l)
    except:
        pass
    
    try:
        if(len(head)<mx):
            head.insert(0, 'Notes')
            y_new[0] = head
    except:
        pass
    try:
        dfs = pd.DataFrame.from_records(y_new)
        dfs.iloc[0][0] = dfs.iloc[0][0].replace(' ', '')
        dfs.columns = dfs.iloc[0]
    except:
        pass
    
    columns = []
    
    for i in range(len(dfs.columns)):
        if(dfs.columns[i] != None):
            columns.append(dfs.columns[i].replace(' ', ''))
        else:
            columns.append(dfs.columns[i])
    dfs.columns = columns
    
    try:
        dfs = dfs.drop(dfs.index[0])

        dfs.reset_index(drop=True, inplace=True)
    except:
        pass
    
    try:
        for i in range(len(dfs['2019'])):
            try:
                dfs['2019'][i] = dfs['2019'][i].replace('-', '')
                dfs['2019'][i] = dfs['2019'][i].replace(' ', '').replace('(', '-').replace(')', '').replace(',', '')
            except:
                pass
            if(dfs['Notes'][i][0] ==  ' '):
                dfs['Notes'][i] = dfs['Notes'][i][1:]
            if(dfs['Notes'][i][len(dfs['Notes'][i])-1] == ' '):
                dfs['Notes'][i] = dfs['Notes'][i][0:len(dfs['Notes'][i])-1]
    except:
        pass
    
    try:
        for i in range(len(dfs['2019'])):
            if(dfs['2019'][i] == None ):
                dfs['2019'][i] = ''
            if(dfs['2019'][i] == '' ):
                dfs['2019'][i] = float("nan")
    except:
        pass
    
    
    try:
        d = dfs.set_index('Notes').to_dict()['2019']
        d = json.dumps(d)
        d = d.replace("\\u00c2", "Â").replace("\\u00a3", "£")
    except:
        pass
    
    if(df['Filename'][z] == name_file) and d != dict_result[z]:
        dict_result.append(d)
    else:
        dict_result.append({float("nan")})
dict_result = dict_result[1:]
df['Extracted Values'] = dict_result
df.to_csv('Submission7.csv', index= False)
print("file saved, work done")