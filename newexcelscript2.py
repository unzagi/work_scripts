import pandas as pd

location = r"C:\Users\sbrooks\Downloads\SxGfL VirginMedia Connections.xlsx"

df = pd.read_excel(location, 0, index_col='Legacy IP Allocations')
df.dtypes
