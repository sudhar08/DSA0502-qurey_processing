
import pandas as pd
import numpy as np
data = np.random.rand(10, 4)
for _ in range(3):
 row, col = np.random.randint(0, 10), np.random.randint(0, 4)
 data[row, col] = np.nan
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
def highlight_nan(val):
 if pd.isna(val):
     return 'background-color:red'
 else:
     return ''
styled_df = df.style.applymap(highlight_nan)
styled_df

