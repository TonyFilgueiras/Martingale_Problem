import pandas as pd

data = {'Times 6 streak appeared': [0],
'Contained a 6 streak': [0],
'Contained a 6 streak %': [0],
'Times 7 streak appeared': [0],
'Contained a 7 streak': [0],
'Contained a 7 streak %': [0],
'Times 8 streak appeared': [0],
'Contained a 8 streak':[0],
'Contained a 8 streak %':[0],
'Times 9 streak appeared': [0],
'Contained a 9 streak':[0],
'Contained a 9 streak %':[0],
'Times 10 streak appeared': [0],
'Contained a 10 streak':[0],
'Contained a 10 streak %':[0],
'Total games played' : [0]
}

df = pd.DataFrame(data)
df.to_csv("coin_flip_results.csv", index=False)

print(df)