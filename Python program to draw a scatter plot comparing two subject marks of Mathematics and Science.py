
import pandas as pd
import matplotlib.pyplot as plt
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data = {'Math Marks': math_marks, 'Science Marks': science_marks, 'Marks Range': marks_range}
df = pd.DataFrame(data)
plt.scatter(df['Marks Range'], df['Math Marks'],label='Math marks', c='red')
plt.scatter(df['Marks Range'], df['Science Marks'], label='Science marks', c='blue')
plt.xlabel('Marks Range')
plt.ylabel('Math and Science Marks')
plt.legend()
plt.show()
