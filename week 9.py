import pandas as pd
data_dict = {
    'Date': [],
    'User': [],
    'Scores': []
}
data_dict['Date'].extend(['2024-04-10', '2024-04-11', '2024-04-11'])
data_dict['User'].extend(['Alice', 'Bob', 'Alice'])
data_dict['Scores'].extend([9, 7, 8])
print("原始数据字典:")
print(data_dict)
original_df = pd.DataFrame()
for key in data_dict:
    original_df[key] = data_dict[key]
print("\n原始DataFrame:")
print(original_df)
pivot_index = 'Date'
pivot_columns = 'User'
pivot_values = 'Scores'
pivoted_df = original_df.pivot(index=pivot_index, columns=pivot_columns, values=pivot_values)
print("\n透视后的DataFrame:")
print(pivoted_df)