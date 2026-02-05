import numpy as np
n=int(input("Enter number of students:"))
studentid = np.arange(1,n+1).reshape(n,1)
print(studentid)
mark1 = np.random.randint(0,100,(n,1))
mark2 = np.random.randint(0,100,(n,1))
mark3 = np.random.randint(0,100,(n,1))
mark4 = np.random.randint(0,100,(n,1))
mark5 = np.random.randint(0,100,(n,1))
mark6 = np.random.randint(0,100,(n,1))
    
grid = np.hstack([studentid, mark1, mark2, mark3, mark4, mark5, mark6])
percent = np.mean(grid[:, 1:], axis=1).reshape(n,1)

print("\nStudent Array used:\n", grid)
print("\nPercent:\n", percent)

total_grid = np.hstack([grid,percent])
print("\nFinal array:\n", total_grid)

student = int(input("Which student do you want to find the marks for?"))
k = total_grid[total_grid[:,0]==student]
print("\nThe marks for the above student are:\n", k)

cls_avg = np.mean(percent)
print("\nClass average =", cls_avg)
print("\nStudents below class average:\n", total_grid[total_grid[:, -1]<cls_avg])
