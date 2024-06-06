import numpy as np
import matplotlib.pyplot as plt

# generate random data for training
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

# add a column of ones for the bias term
X = np.hstack((np.ones((100, 1)), x))

# calculate the weights using the normal equation
weights = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# make predictions using the calculated weights
predictions = X.dot(weights)

# plot the original data and the predictions
plt.scatter(x, y, color='green')
plt.plot(x, predictions, color='red')
plt.show()
