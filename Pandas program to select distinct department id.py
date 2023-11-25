import pandas as pd
employees = pd.read_csv(r"C:\Users\LENOVO\Desktop\New folder\lab 1 query.csv")
distinct_department_ids = employees['DEPARTMENT_ID'].unique()
print(distinct_department_ids)
