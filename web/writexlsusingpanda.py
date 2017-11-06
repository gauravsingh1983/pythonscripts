from pandas import DataFrame
import openpyxl

l1 = [[1,2,3,4],[3,2,4,5]]

df = DataFrame({'Stimulus Time': l1[0], 'Reaction Time': l1[1]})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
print(df)