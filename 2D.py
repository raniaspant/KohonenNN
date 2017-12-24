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
    if y <= 1 - x:  # Specify their region
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


# Calculate and store the distance between each input and weight point

for i in range(0, 1000):
    for j in range(0, 100):
        distances[i, j] = math.sqrt(math.pow((inputs[i, 0] - weights[j, 0]), 2)
                                    + math.pow((inputs[i, 1] - weights[j, 1]), 2))

t = 0
weightsX = np.reshape(weights[:, 0], (10, 10))
weightsY = np.reshape(weights[:, 1], (10, 10))
plt.figure(1)
plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
plt.plot(weightsX, weightsY, 'r')

while t < T:
    print("iteration: ", t)
    if t == 200:
        plt.figure(2)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        for a in range(0, 10):
            plt.plot(weightsX[a, :], weightsY[a, :], 'r')
        for a in range(0, 10):
            plt.plot(weightsX[:, a], weightsY[:, a], 'r')
    if t == 400:
        plt.figure(3)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        for a in range(0, 10):
            plt.plot(weightsX[a, :], weightsY[a, :], 'r')
        for a in range(0, 10):
            plt.plot(weightsX[:, a], weightsY[:, a], 'r')
    if t == 600:
        plt.figure(4)
        plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
        for a in range(0, 10):
            plt.plot(weightsX[a, :], weightsY[a, :], 'r')
        for a in range(0, 10):
            plt.plot(weightsX[:, a], weightsY[:, a], 'r')
    for i in range(0, 1000):
        d = round(d0 * (1 - t / T))
        eta = eta0 * (1 - t / T)
        row = distances[i, :].tolist()
        jStar = min(row)
        index = row.index(jStar)
        if math.floor(index / 10) == 0:  # one digit number
            X = 0
            Y = index
        elif math.floor(index / 10) != 0 and index % 10 == 0:  # 10 multiplier
            X = math.floor(index / 10)
            Y = 9
        else:
            X = math.floor(index / 10)
            Y = index % 10
        neighbourhoodX = []
        neighbourhoodY = []
        ii = Y
        jj = 0
        while ii >= 0 and jj <= d:  # find all the neighbours from the left side
            neighbourhoodX.append(ii)
            ii -= 1
            jj += 1
        ii = Y + 1
        jj = 1
        while ii <= 9 and jj <= d:  # find all the neighbours from the right side
            neighbourhoodX.append(ii)
            ii += 1
            jj += 1
        # now time to find neighbours on the same column Y, so up and down from j*
        ii = X + 1
        jj = 1
        while ii <= 9 and jj <= d:  # find all the neighbours below j*
            neighbourhoodY.append(ii)
            ii += 1
            jj += 1
        ii = X - 1
        jj = 1
        while ii >= 0 and jj <= d: # find all the neighbours above j*
            neighbourhoodY.append(ii)
            ii -= 1
            jj += 1
        # by now neighbourhood[] should contain the j* neighbourhood
        for ii in range(0, len(neighbourhoodY)):  # for each neighbour on the same column
            DWx = eta * (inputs[i, 0] - weightsX[neighbourhoodY[ii], Y])
            DWy = eta * (inputs[i, 1] - weightsY[neighbourhoodY[ii], Y])
            weightsX[neighbourhoodY[ii], Y] += DWx
            weightsY[neighbourhoodY[ii], Y] += DWy
        for ii in range(0, len(neighbourhoodX)):  # for each neighbour on the same row
            DWx = eta * (inputs[i, 0] - weightsX[X, neighbourhoodX[ii]])
            DWy = eta * (inputs[i, 1] - weightsY[X, neighbourhoodX[ii]])
            weightsX[X, neighbourhoodX[ii]] += DWx
            weightsY[X, neighbourhoodX[ii]] += DWy
        cols = 0
        for jj in range(0, 10):
            for kk in range(0, 10):
                distances[i, cols] = math.sqrt(math.pow((inputs[i, 0] - weightsX[jj, kk]), 2) +
                                               math.pow((inputs[i, 1] - weightsY[jj, kk]), 2))
                cols += 1
    t += 1

plt.figure(5)
plt.plot(inputs[:, 0], inputs[:, 1], 'bd')
for a in range(0, 10):
    plt.plot(weightsX[a, :], weightsY[a, :], 'r')
for a in range(0, 10):
    plt.plot(weightsX[:, a], weightsY[:, a], 'r')
plt.show()
