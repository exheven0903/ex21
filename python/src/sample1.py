import matplotlib.pyplot as plt
import numpy as np

# x軸:時刻
X = np.arrange(0, 100, 0.5)

# y軸:sin波
Hz = 5.
y = np.sin(2.0 * np.pi * (X * Hz) / 100)

# グラフの描画
plt.plot(X, y)
plt.savefig('test.png')