import numpy as np
rain = np.random.randint(0,1000,(5,6))
print("Rain Data for 6 months from 5 states:\n", rain, "\n")
print("Average rainfall for each month:", rain.mean(axis=0), "\n")
for i in range(6):
    print("Data for month", i+1, "is:\n", rain[:, i:i+1])