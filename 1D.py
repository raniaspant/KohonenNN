import numpy as np
import random
import math
import matplotlib.pyplot as plt

inputs = np.zeros((1000, 2))
weights = np.zeros((100, 2))
distances = np.zeros((1000, 100))
d0 = 3
eta0 = 0.1
T = 1000
# Generate randomly the input points
c = 0
while c < 1000:
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if y <= 1 - x:       # Specify their region
        inputs[c, 0] = x
        inputs[c, 1] = y
        c += 1


# Generate randomly the weight points

c = 0
while c < 100:
    wx = random.uniform(0.2, 0.3)
    wy = random.uniform(0.2, 0.3)
    weights[c, 0] = wx
    weights[c, 1] = wy
    c += 1
    
plt.figure(1)
plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
plt.plot(weights[:, 0], weights[:, 1], 'r')
# Calculate and store the distance between each input and weight point

for i in range(0, 1000):
    for j in range(0, 100):
        distances[i, j] = math.sqrt(math.pow((inputs[i, 0] - weights[j, 0]), 2)
                                    + math.pow((inputs[i, 1] - weights[j, 1]), 2))

t = 0

while t < T:
    print("iteration: ", t)
    if t == 200:
        plt.figure(2)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        plt.plot(weights[:, 0], weights[:, 1], 'r')
    if t == 400:
        plt.figure(3)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        plt.plot(weights[:, 0], weights[:, 1], 'r')
    if t == 600:
        plt.figure(4)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        plt.plot(weights[:, 0], weights[:, 1], 'r')
    for i in range(0, 1000):
        d = round(d0 * (1 - t / T))
        eta = eta0 * (1 - t / T)
        row = distances[i, :].tolist()
        jStar = min(row)
        index = row.index(jStar)
        neighbourhood = []
        ii = index
        jj = 0
        while ii >= 0 and jj <= d:  # find all the neighbours from the left side + jStar
            neighbourhood.append(ii)
            ii -= 1
            jj += 1
        ii = index + 1
        jj = 1
        while ii < 100 and jj <= d:  # find all the neighbours from the right side
            neighbourhood.append(ii)
            ii += 1
            jj += 1
        # by now neighbourhood[] should contain the j* neighbourhood
        for ii in range(0, len(neighbourhood)):  # for each neighbour
            DWx = eta * (inputs[i, 0] - weights[neighbourhood[ii], 0])
            DWy = eta * (inputs[i, 1] - weights[neighbourhood[ii], 1])
            weights[neighbourhood[ii], 0] = weights[neighbourhood[ii], 0] + DWx
            weights[neighbourhood[ii], 1] = weights[neighbourhood[ii], 1] + DWy
        for jj in range(0, 100):
            distances[i, jj] = math.sqrt(math.pow((inputs[i, 0] - weights[jj, 0]), 2) +
                                         math.pow((inputs[i, 1] - weights[jj, 1]), 2))
    t += 1

plt.figure(5)
plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
plt.plot(weights[:, 0], weights[:, 1], 'r')
plt.show()
