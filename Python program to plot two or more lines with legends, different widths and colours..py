import pandas as pd
import matplotlib.pylab as plt
x1=[12,33,45]
y1=[21,4,42]
x2=[21,4,42]
y2=[12,33,45]
plt.plot(x1,y1,c='red',label='x')
plt.plot(x2,y2,c='blue',label='y')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
