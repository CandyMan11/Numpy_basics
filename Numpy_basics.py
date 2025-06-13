# %%
import numpy as np

# %%
marks = np.random.randint(0, 101, size=30)
print(marks)

# %%
avg = np.mean(marks)
max_score = np.max(marks)
min_score = np.min(marks)
print(f"Average_score: {round(avg, 3)}\nMax_score: {max_score}\nMin_score: {min_score}")


# %%
sorted_marks = np.sort(marks)
print(f"Top 5 scores: {sorted_marks[-5:]}")

# %%
condition = marks > 50
print(f"Number of students with marks greater than 50: {np.sum(condition)}")

# %%
#reshaping
reshaped_marks = marks.reshape(6, 5)
print(reshaped_marks)

# %%
for i in range(0, len(reshaped_marks)):
    print(f"Row {i+1} avg: {np.mean(reshaped_marks[i])}")

