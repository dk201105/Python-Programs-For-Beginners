import numpy as np
sales = np.random.randint(500,1000,(5,12))
print("Original Array:\n",sales)

q_sales = sales.reshape(5,4,3).sum(axis=2)
print("\n Total Quarterly sales\n",q_sales)

lesser=np.sum(sales<600, axis=1)
print("\nLesser than 600\n",lesser)

avg_col=np.mean(sales,axis=1).reshape(5,1)
new_array=np.hstack([sales, avg_col])
print("\nNew Array with average price\n",new_array)
