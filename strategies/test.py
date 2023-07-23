import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
x = np.random.randn(100)
y = np.random.randn(100)
sns.kdeplot(x, y, fill=True)

plt.figure(figsize=(200, 100))
plt.show()
