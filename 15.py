import pandas as pd
import numpy as np
data = {
    'ord_no': [np.nan, np.nan, 'Ө', 1, np.nan, 270.65, '2012-09-10', 3001.0, 70002.0, 65.26, np.nan],
    'purch_amt': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'ord_date': [np.nan, np.nan, np.nan, np.nan, 948.50, '2012-09-10', 3002.0, 70005.0, 2400.60, '2012-07-27', 3001.0],
    'customer_id': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
}
df = pd.DataFrame(data)
df = df.dropna(thresh=2)
print(df)
