import numpy as np

vector  = np.array([1, 2, 3, 4, 5])
print("Created vector:", vector)


vector = np.arange(2, 11, 2)
print("New vector is", vector)


vector = np.random.rand(5)
print("5 random decimals numbers:", vector)


#practice
vector = np.random.rand(7)
print("7 random decimals:", vector)

vector = np.random.rand(77)
print("77 random decimal numbers:", vector)



vector = np.linspace(0, 1, 6)
print("vector of 6 equally spaced values:", vector)


vector = np.linspace(2, 4, 12)
print(vector)



vector = np.full(5, 7)
print("vector with 7", vector)



vector = np.concatenate((np.zeros(4), np.ones(3)))
print(vector)


#Practice:
vector = np.concatenate((np.zeros(100), np.ones(500)))
print(vector)

vector = np.concatenate((np.zeros(1000), np.ones(10000)))
print(vector)

vector = np.concatenate((np.ones(54), np.zeros(433)))
print(vector)
