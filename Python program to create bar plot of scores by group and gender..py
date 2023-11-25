
import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)
x = np.arange(len(groups))
bar_width = 0.35
plt.bar(x - bar_width/2, men_means, bar_width, label='Men', color='green')
plt.bar(x + bar_width/2, women_means, bar_width, label='Women', color='red')
plt.xlabel('Groups')
plt.xticks(x, groups)
plt.title('Scores by Group and Gender')
plt.ylabel('Scores')
plt.legend()
plt.show()
