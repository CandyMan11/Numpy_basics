# 📊 NumPy Mini Projects

This repository contains two simple Python mini-projects demonstrating the use of NumPy for basic data analysis and simulation:

1. **Student Marks Analysis**
2. **Coin Toss Simulation**

---

## 📘 1. Student Marks Analysis

### Description:
This script performs basic statistical analysis on a randomly generated list of 30 student marks using NumPy.

### Features:
- Generate 30 random marks between 0 and 100.
- Calculate:
  - Average score
  - Maximum and minimum score
- Display the top 5 scores.
- Count number of students scoring above 50.
- Reshape marks into a 6x5 matrix and compute row-wise averages.

---

## 🪙 2. Coin Toss Simulation

### Description:
This script simulates 1000 coin tosses using NumPy and counts how many times heads and tails occur.

### Features:
- Generate 1000 random tosses (0 = Heads, 1 = Tails).
- Use boolean indexing to count heads and tails.

---

## 📦 Requirements

- Python 3.x
- NumPy

Install NumPy with:

```bash
pip install numpy
```

---

## ▶️ How to Run

```bash
python marks_analysis.py
python coin_toss.py
```

---

## 📁 Folder Structure

```
📂 numpy-mini-projects
├── marks_analysis.py
├── coin_toss.py
└── README.md
```

---

## 🧠 Learning Outcome

These projects introduce:
- Random data generation with `numpy.random`
- Basic statistics using NumPy functions
- Boolean masking
- Matrix reshaping and row-wise operations
