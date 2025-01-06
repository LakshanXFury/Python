"""
The merge() function in Pandas is used to combine two DataFrames based on a common key (or multiple keys).
It works similarly to SQL joins, allowing you to merge data horizontally by aligning rows based on key columns.

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False)

Parameters
left: The left DataFrame.
right: The right DataFrame.
how: The type of merge to perform:
'inner' (default): Only matching rows in both DataFrames.
'outer': All rows from both DataFrames, filling in NaN for missing matches.
'left': All rows from the left DataFrame and matching rows from the right.
'right': All rows from the right DataFrame and matching rows from the left.
on: Column name(s) to join on. Must be present in both DataFrames.
left_on / right_on: Column name(s) in the left/right DataFrame to join on.
left_index / right_index: Use the index from the left/right DataFrame as the key(s).
sort: Sort the result by the join keys (default is False).
"""

import pandas as pd

# DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Score': [85, 90, 75]
})

# Merge on 'ID'
result = pd.merge(df1, df2, on='ID', how='inner')
print(result)

#Outer Merge - Will give NAN values
result = pd.merge(df1, df2, on='ID', how='outer')
print(result)

