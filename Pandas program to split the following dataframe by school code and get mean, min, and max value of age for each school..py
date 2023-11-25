import pandas as pd
data = {
    'school': ['s001', 's002', 's003', 's001', 's002', 'S004', 's001', 'S004', 's002', 's001'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes', 'Alberto Franco', 'David Parkes', 'Gino Mcneill', 'Alberto Franco'],
    'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997', '15/05/2002', '15/09/1997', '17/05/2002', '15/05/2002'],
    'age': [12, 13, 12, 13, 14, 13, 12, 13, 12, 13],
    'height': [173, 192, 186, 167, 151, 159, 173, 159, 192, 173],
    'weight': [35, 32, 33, 30, 31, 32, 35, 32, 32, 35],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4', 'street1', 'street4', 'street2', 'street1']
}
df = pd.DataFrame(data)
result = df.groupby('school')['age'].agg(['mean', 'min', 'max'])
print(result)
