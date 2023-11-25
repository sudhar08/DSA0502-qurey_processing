import pandas as pd
import numpy as np
data = np.random.randn(10, 4) 
df = pd.DataFrame(data, columns=['B', 'C', 'D','E'])
def highlight_numbers(val):
 color = 'red' if val < 0 else 'black'
 return f'color: {color}'
styled_df = df.style.applymap(highlight_numbers)
styled_df

