import pandas as pd
import matplotlib.pylab as plt
data={'Date':['10-03-2016','10-04-2016','10-05-2016','10-06-2016','10-07-2016'],
 'Open':[774.25,776.030029,779.309998,779,779.659973],
 'High':[776.065002,778.710022,782.070007,780.47998,779.659973],
 'Low':[769.5,772.890015,775.650024,775.539978,770.75],
 'Close':[772.559998,776.429993,776.469971,776.859985,775.080017]}
df=pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
df.plot()
plt.show()
