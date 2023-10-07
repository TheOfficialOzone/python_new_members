

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Run this code using 'python3 part2.py'

# SCENARIO: We are analyzing the speed of a Jeep Liberty 2006
# The data is the speed we have logged off a drag strip

# Answer the following question:
#   Why does the speed have Jagged edges?

data = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00, 24.00, 25.00, 26.00, 27.00, 26.00, 27.00, 28.00, 29.00, 30.00, 31.00, 32.00, 33.00, 34.00, 35.00, 36.00, 37.00, 38.00, 39.00, 40.00, 39.00, 40.00, 41.00, 42.00, 43.00, 44.00, 45.00, 46.00, 47.00, 48.00, 49.00, 50.00, 51.00, 52.00, 53.00, 52.00, 53.00, 54.00, 55.00, 56.00, 57.00, 58.00, 59.00, 60.00, 61.00, 62.00, 63.00, 64.00, 65.00, 66.00, 65.00, 66.00, 67.00, 68.00, 69.00, 70.00, 71.00, 72.00, 73.00, 74.00, 75.00, 76.00, 77.00, 78.00, 79.00, 78.00, 79.00, 80.00, 81.00, 82.00, 83.00, 84.00, 85.00, 86.00, 87.00]

plt.plot(data)
plt.ylabel('Speed (km/h)')
plt.xlabel('Time (s)')
plt.show()
