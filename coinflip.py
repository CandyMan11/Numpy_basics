import numpy as np

toss = np.random.randint(0, 2, 1000)

#condition 1
heads = toss == 0

#condition 2
tails = toss == 1

print(f"Heads: {np.sum(heads)}")
print(f"Tails: {np.sum(tails)}")
