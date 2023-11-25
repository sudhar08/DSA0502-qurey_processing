import pandas as pd
import numpy as np
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
def apply_colors(val):
 return f'background-color: black; color: yellow'
styled_df = df.style.applymap(apply_colors)
styled_df
