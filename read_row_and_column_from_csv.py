import pandas as pd

df=pd.read_csv("/home/ajay/Documents/Oodles_projects/Hey_kaido/kaido-web-app/kaido/gift_data.csv")
total_row=len(df.axes[0])
total_column=len(df.axes[1])
print("column",total_column)
print("total_row",total_row)