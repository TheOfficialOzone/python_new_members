
import matplotlib.pyplot as plt

# Run this python code using: python3 part1.py
# You may need in install numpy and matplotlib using pip
# Run the program once without making any changes

# GOAL: Smooth out this data, as it is quite noisy using a rolling average
# Your graph should be less jittery as a result, (Note you should have less than 100 data points once you have performed a rolling average)

data = [4.00, -3.43, -1.86, 3.71, 8.28, 6.85, 5.41, 12.97, 10.53, 15.09, 19.64, 18.19, 21.74, 23.28, 23.81, 23.34, 22.87, 28.39, 29.90, 28.40, 34.90, 33.39, 32.87, 38.35, 33.81, 36.27, 36.71, 42.15, 45.58, 41.99, 40.40, 44.79, 50.18, 47.55, 45.90, 55.25, 54.58, 50.90, 58.21, 53.50, 54.78, 57.04, 64.29, 64.52, 61.74, 65.94, 67.13, 64.30, 64.45, 66.59, 74.71, 70.81, 75.90, 76.96, 76.01, 74.04, 72.05, 77.04, 80.02, 78.97, 77.90, 77.81, 85.71, 79.58, 85.43, 85.26, 87.07, 85.86, 90.63, 88.38, 85.10, 91.80, 91.48, 94.14, 86.78, 89.39, 93.98, 92.54, 94.09, 97.61, 99.11, 96.58, 93.03, 98.46, 91.86, 98.24, 99.59, 92.92, 102.23, 98.51, 100.77, 103.00, 97.21, 96.40, 102.56, 98.69, 102.80, 99.89, 95.95, 102.99]

plt.plot(data)
plt.ylabel('Speed')
plt.show()
