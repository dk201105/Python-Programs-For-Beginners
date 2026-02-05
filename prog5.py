import numpy as np
bags = np.random.randint(1, 50, (5,3))
print("No. of balls in each bag:\n", bags, "\n")
print("Bags with more red than green:", np.where(bags[:,0]>bags[:,1][0]+1))
bags[0,1]+=5
bags[2,0]-=3
print("\n Updated Balls:\n", bags)
print("\nTotal balls:", bags.sum())