
"""
Docstring for creating_a _vector

NumPy (Numerical Python) is the backbone of scientific computing in Python. It is a powerful, fast, and flexible library designed to handle large amounts of numerical data efficiently. Before NumPy, Python was great for logic and scripting, but when it came to heavy math and large-scale numerical operations, it was slow and clumsy. NumPy changed the game by bringing speed, structure, and serious mathematical power into Python.
At the heart of NumPy is the ndarray (N-dimensional array). This is a special data structure that looks like a list, but it is much faster, more memory-efficient, and built specifically for numerical work. Unlike normal Python lists, NumPy arrays store data in a continuous block of memory, which allows the computer to perform operations on entire arrays at once instead of looping element by element. This idea is called vectorization, and it is one of the main reasons NumPy is so fast.

NumPy supports arrays of any dimension:

1D arrays for vectors

2D arrays for matrices or tables

3D and higher for images, videos, scientific simulations, and deep learning data

With NumPy, you can create arrays from lists, ranges, random numbers, files, or even other libraries. Once created, you can reshape them, slice them, filter them, and perform complex operations in just one line of code.

One of NumPy’s biggest strengths is its huge collection of mathematical functions. It provides built-in support for:

Basic arithmetic (add, subtract, multiply, divide)

Linear algebra (dot product, matrix multiplication, eigenvalues, determinants)

Statistics (mean, median, variance, standard deviation)

Trigonometry (sin, cos, tan)

Exponentials and logarithms

Random number generation for simulations and ML

All these operations work directly on whole arrays, not just single numbers. That means you can apply a formula to millions of values instantly, without writing slow loops.

NumPy also plays the role of a foundation library. Many famous Python libraries are built on top of it, including:

  Pandas for data analysis
  Matplotlib and Seaborn for visualization
  SciPy for advanced scientific computing
  Scikit-learn for machine learning
  TensorFlow and PyTorch for deep learning

If you understand NumPy well, learning these libraries becomes much easier because they all use NumPy arrays under the hood.

Another important feature of NumPy is broadcasting. Broadcasting allows NumPy to perform operations between arrays of different shapes in a smart way, without manually copying data. For example, you can add a single number to a whole matrix, or add a vector to every row of a matrix, and NumPy will automatically handle the alignment. This makes code shorter, cleaner, and more readable.

NumPy is also memory-efficient. It allows you to choose data types like int32, float64, bool, etc., so you can control how much memory your data uses. This is very important when working with big datasets, images, or scientific simulations.
    In real life, NumPy is used everywhere:
    In data science to clean and transform data
    In machine learning to prepare features and labels
    In bioinformatics to analyze genetic and biological data
    In finance for risk analysis and simulations
    In engineering for signal and image processing
    In physics and chemistry for modeling and experiments
In simple words, NumPy turns Python into a powerful numerical engine. It removes the pain of slow loops, messy math, and inefficient data handling. Once you master NumPy, you unlock the real power of Python for data science, AI, scientific research, and high-performance computing. That’s why every serious data scientist, machine learning engineer, and researcher starts their journey with NumPy.
"""
import numpy as np

#create a vector using numpy
vector  = np.array([1, 2, 3, 4, 5])
print("Created vector:", vector)

# Problem 1:

# Ek vector banao jo 1 se 10 tak ke even numbers store kare.
vector = np.arange(2, 11, 2)
print("New vector is", vector)

"""
Discussion:
  Yahan np.arange(start, stop, step) use hua:
  start = 2
  stop = 11 (11 isliye diya kyun ke stop include nahi hota)
  step = 2
Is se humein automatically even numbers mil gaye bina loop likhe. Traditional tareeqa hota loop se, lekin NumPy ka style fast aur clean hota hai."""

# Problem 2:

# Ek vector banao jismein 5 random decimal numbers hon jo 0 aur 1 ke beech hon.

vector = np.random.rand(5)
print("5 random decimals numbers:", vector)

"""
Discussion:
  np.random.rand(5) ka matlab:
  5 random values generate karo
  Har value 0 aur 1 ke beech hogi
Har dafa code chalane par different values aayengi. Ye technique machine learning, simulations, aur testing ke liye bohat use hoti hai, jahan dummy data chahiye hota hai."""

#practice
vector = np.random.rand(7)
print("7 random decimals:", vector)

vector = np.random.rand(77)
print("77 random decimal numbers:", vector)

# Problem 3

# 0 se 1 tak 6 equally spaced values ka vector banao.

vector = np.linspace(0, 1, 6)
print("vector of 6 equally spaced values:", vector)

"""
Discussion:

linspace(start, end, count) use hota hai jab tumhein range ko barabar parts mein divide karna ho. Ye data visualization aur scientific experiments mein bohat kaam aata hai."""

#pratice:
vector = np.linspace(2, 4, 12)
print(vector)


# Problem 4

# Ek vector banao jismein sab values 7 hon, length 5.

vector = np.full(5, 7)
print("vector with 7", vector)

"""
Discussion:

np.full(size, value) tab use hota hai jab tumhein same value se initialize karna ho, jaise default weights, masks, ya placeholders."""


# Problem 5

# Ek vector banao jismein pehle 4 zeros aur baqi 3 ones hon.

vector = np.concatenate((np.zeros(4), np.ones(3)))
print(vector)

"""
Discussion:

zeros() aur ones() se simple vectors bante hain. concatenate() unhein jor kar complex structure banata hai. Ye technique labels aur flags banane mein kaam aati hai."""

#Practice:
vector = np.concatenate((np.zeros(100), np.ones(500)))
print(vector)

vector = np.concatenate((np.zeros(1000), np.ones(10000)))
print(vector)

vector = np.concatenate((np.ones(54), np.zeros(433)))
print(vector)
