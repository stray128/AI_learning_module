# Data Science Learning Module

A hands-on practice system with **~340 problems** designed to build your data science skills from the ground up.

## Why This Module?

Data science isn't learned by reading - it's learned by doing. This module provides structured practice with immediate feedback, taking you from Python basics to complete data analysis workflows.

**What makes this effective:**
- Problems build on each other progressively
- Instant feedback tells you if you're on the right track
- Real-world datasets prepare you for actual data science work
- Capstone projects tie everything together

---

## Learning Path

Complete the modules in order. Each one builds on skills from previous modules.

| Module | Notebooks | Problems | What You'll Master |
|--------|-----------|----------|-------------------|
| [01 - OS Module](01_os_module/) | 3 | ~45 | File handling, directories, paths |
| [02 - NumPy](02_numpy/) | 4 | ~80 | Numerical computing, arrays, vectorization |
| [03 - Pandas](03_pandas/) | 4 | ~80 | Data manipulation, cleaning, analysis |
| [04 - Matplotlib](04_matplotlib/) | 3 | ~45 | Data visualization, charts, dashboards |
| [05 - Sklearn Stats](05_sklearn_stats/) | 3 | ~50 | Statistics, preprocessing, encoding |
| [06 - EDA Integration](06_eda_integration/) | 2 | ~40 | Combined analysis workflows |
| [07 - Capstone Projects](07_capstone_projects/) | 2 | ~30 | Real-world data challenges |

---

## Getting Started

### Step 1: Set Up Your Environment

```bash
# Install required packages
pip install -r requirements.txt

# Download the datasets (run once)
cd datasets && python download_datasets.py
```

### Step 2: Launch Jupyter

```bash
jupyter notebook
```

### Step 3: Begin Learning

1. Navigate to `01_os_module/`
2. Open `01_file_operations.ipynb`
3. Read the README in each module folder for guidance

---

## How to Use Each Notebook

Every problem follows this structure:

### 1. Concept Section
Explains the skill you're practicing with syntax examples.

### 2. Task Description
Tells you exactly what to build or compute.

### 3. Solution Cell
Where you write your code. Variables are often pre-defined for you.

### 4. Verification Cell
Run this to check your answer. You'll see:
- ✓ **PASSED** - You got it right!
- ✗ **FAILED** - Try again, with a hint about what's wrong

### 5. Summary (end of notebook)
Shows your overall progress on that notebook.

---

## Difficulty Progression

Each notebook ramps up gradually:

| Level | Problems | What to Expect |
|-------|----------|----------------|
| **Easy** | First 5-7 | Direct application of concepts, 1-2 lines |
| **Medium** | Middle section | Combining concepts, 3-5 lines |
| **Hard** | Last 5-7 | Multi-step solutions, edge cases |

Don't skip the easy problems - they build the foundation for harder ones.

---

## Module Highlights

### Module 1: Python OS Module
Work with files and directories programmatically. Essential for automating data pipelines.

### Module 2: NumPy
The backbone of scientific Python. Learn vectorized operations that are 100x faster than loops.

### Module 3: Pandas
The tool you'll use daily as a data scientist. Master DataFrames, filtering, grouping, and merging.

### Module 4: Matplotlib
Turn data into visual stories. Create publication-quality charts and multi-panel dashboards.

### Module 5: Statistics & Preprocessing
Prepare data for machine learning. Scale features, encode categories, and split data properly.

### Module 6: EDA Integration
Combine all skills into complete analysis workflows that mirror real data science work.

### Module 7: Capstone Projects
Apply everything to real datasets. Analyze Titanic survival data and clean messy real-world data.

---

## Datasets

### Synthetic Data (`datasets/synthetic/`)
Controlled datasets designed for learning specific concepts. Predictable patterns help you verify your understanding.

### Real Data (`datasets/public/`)
- **Titanic** - Passenger survival data (classification)
- **Tips** - Restaurant tipping data (regression/exploration)
- **Iris** - Classic flower measurements (clustering/classification)

---

## Tips for Success

1. **Don't skip ahead** - Skills build on each other
2. **Try before checking** - Struggle is part of learning
3. **Read error messages** - They tell you what's wrong
4. **Use the hints** - Problem descriptions contain clues
5. **Review passed problems** - Understanding why you're right matters
6. **Take breaks** - Let concepts sink in between sessions

---

## When You Get Stuck

1. Re-read the **Concept** and **Syntax** sections
2. Check the **Example** - it often shows exactly what you need
3. Look at similar problems you've already solved
4. Review the module's README for context
5. Search the error message online

---

## What's Next?

After completing all modules, you'll be ready to:

- **Analyze your own datasets** with confidence
- **Clean messy real-world data** systematically
- **Create visualizations** that communicate insights
- **Prepare data for machine learning** properly
- **Take on Kaggle competitions** and real data challenges

---

Good luck, and enjoy the journey into data science!
