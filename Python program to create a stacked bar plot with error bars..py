
import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
men_scores = [85, 78, 92, 88, 76]
women_scores = [78, 86, 90, 83, 79]
men_errors = [2, 3, 4, 2, 3]
women_errors = [2, 3, 4, 2, 3]
x = np.arange(len(groups))
bar_width = 0.35
plt.bar(x, men_scores, bar_width, label='Men', color='green', yerr=men_errors, capsize=5)
plt.bar(x, women_scores, bar_width, label='Women', color='red', yerr=women_errors, capsize=5, bottom=men_scores)
plt.xlabel('Groups')
plt.xticks(x, groups)
plt.title('Stacked Bar Plot with Error Bars')
plt.ylabel('Scores')
plt.legend()
plt.show()
