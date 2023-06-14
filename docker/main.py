import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

print("Plotting graph........")

dist = np.random.standard_normal(100000)
fig = px.histogram(dist, nbins = 30)

plt.hist(dist, bins=20)
plt.show()
fig.show()