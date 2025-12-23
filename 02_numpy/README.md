# Module 2: NumPy Fundamentals

Master numerical computing with NumPy - the foundation of Python's data science ecosystem.

## What You'll Learn

NumPy provides efficient array operations that are 10-100x faster than Python lists. This module builds your skills from basic array creation to advanced statistical operations.

## Notebooks

### 1. Array Creation (`01_array_creation.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Medium

Build arrays from scratch and understand their structure:
- Creating arrays from lists and ranges
- Generating arrays with `zeros`, `ones`, `full`, and `empty`
- Using `arange` and `linspace` for sequences
- Creating random arrays (uniform, normal distributions)
- Reshaping and understanding array dimensions
- Working with data types (`dtype`)

**Practical Application:** Initialize data structures for simulations, create test datasets, and prepare data containers for analysis.

---

### 2. Indexing & Slicing (`02_indexing_slicing.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Hard

Access and extract data efficiently:
- Basic indexing for 1D and 2D arrays
- Slicing with start, stop, and step
- Boolean indexing (filtering with conditions)
- Fancy indexing (selecting with arrays)
- Combining multiple indexing techniques
- Views vs. copies

**Practical Application:** Filter datasets, extract subsets for analysis, and manipulate specific data regions.

---

### 3. Operations & Broadcasting (`03_operations_broadcasting.ipynb`)
**Problems:** 20 | **Difficulty:** Medium to Hard

Perform efficient element-wise and matrix operations:
- Arithmetic operations (+, -, *, /, **)
- Comparison operations and logical operators
- Broadcasting rules for arrays of different shapes
- Aggregation functions (sum, mean, min, max)
- Axis-based operations
- Matrix operations (dot product, transpose)

**Practical Application:** Perform batch calculations on entire datasets without loops, normalize data, and implement mathematical formulas.

---

### 4. Statistics & Linear Algebra (`04_statistics_linalg.ipynb`)
**Problems:** 20 | **Difficulty:** Medium to Hard

Apply statistical and mathematical operations:
- Descriptive statistics (mean, median, std, variance)
- Percentiles and quantiles
- Correlation and covariance
- Matrix operations (inverse, determinant, eigenvalues)
- Solving linear equations
- Random sampling and distributions

**Practical Application:** Calculate summary statistics, perform correlation analysis, and prepare data for machine learning.

---

## Prerequisites

- Completion of Module 1 (OS Module) recommended
- Basic understanding of mathematical operations
- Familiarity with matrices and vectors helpful

## Key Concepts

| Concept | Why It Matters |
|---------|----------------|
| Vectorization | Avoid slow Python loops; let NumPy optimize |
| Broadcasting | Apply operations across arrays of different shapes |
| Views vs Copies | Understand memory efficiency and avoid bugs |
| Axis Parameter | Control whether operations work on rows or columns |

## Getting Started

1. Open `01_array_creation.ipynb`
2. Run the setup cell to import NumPy
3. Work through problems sequentially - they build on each other
4. Pay attention to the shape of arrays at each step

## Tips for Success

- Print array shapes frequently with `arr.shape`
- Use `arr.dtype` to check data types
- When stuck, visualize small arrays to understand the operation
- Remember: axis=0 operates along rows, axis=1 along columns
