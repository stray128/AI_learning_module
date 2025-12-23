# Module 6: EDA Integration

Combine all your skills into complete exploratory data analysis workflows.

## What You'll Learn

This module brings together NumPy, Pandas, Matplotlib, and statistics into cohesive analysis pipelines. You'll practice the full EDA workflow that data scientists use daily.

## Notebooks

### 1. NumPy & Pandas Combined (`01_numpy_pandas_combo.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Hard

Leverage both libraries together for efficient analysis:
- Converting between DataFrames and NumPy arrays
- Applying NumPy functions to Pandas columns
- Using `np.where()` and `np.select()` for conditional logic
- Broadcasting operations on DataFrames
- Vectorized string operations
- Rolling window calculations
- Z-score and outlier detection
- Binning continuous data with `pd.cut()`
- Cumulative operations and ranking
- Group-wise percentage calculations

**Practical Application:** Build efficient data transformations that combine the best of both libraries.

---

### 2. Full EDA Workflow (`02_full_eda_workflow.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Hard

Execute a complete exploratory analysis from start to finish:
- **Data Loading:** Read and initial inspection
- **Missing Data Analysis:** Count, percentage, visualization
- **Statistical Summaries:** Descriptive stats for numeric and categorical
- **Visualization:** Histograms, box plots, scatter plots, bar charts
- **Group Analysis:** Statistics by category
- **Feature Engineering:** Creating derived features
- **Multi-Panel Dashboards:** Comprehensive visual summaries
- **Filtering & Subsetting:** Deep dives into data segments
- **Reusable EDA Functions:** Automate common tasks

**Practical Application:** Develop a systematic approach to understanding any new dataset.

---

## Prerequisites

- Completion of Modules 1-5
- Familiarity with all core libraries (NumPy, Pandas, Matplotlib)

## The EDA Workflow

```
1. Load Data
   └── Read file, check shape, preview rows

2. Understand Structure
   └── Data types, column names, memory usage

3. Assess Quality
   └── Missing values, duplicates, outliers

4. Statistical Summary
   └── Describe numerics, value counts for categories

5. Visualize Distributions
   └── Histograms, box plots for each variable

6. Explore Relationships
   └── Scatter plots, correlation matrix, group comparisons

7. Feature Engineering
   └── Create derived variables, bin continuous data

8. Document Findings
   └── Key insights, data quality issues, next steps
```

## Key Techniques

| Task | Technique |
|------|-----------|
| Quick conditional column | `np.where(condition, if_true, if_false)` |
| Multiple conditions | `np.select(conditions, choices)` |
| Outlier detection | IQR method: `Q1 - 1.5*IQR` to `Q3 + 1.5*IQR` |
| Binning | `pd.cut(data, bins, labels)` |
| Rolling stats | `series.rolling(window).mean()` |
| Group percentages | `df.groupby('cat')['val'].transform('sum')` |

## Getting Started

1. Open `01_numpy_pandas_combo.ipynb`
2. Practice combining techniques you learned in previous modules
3. Move to `02_full_eda_workflow.ipynb` for complete analysis practice
4. Use real datasets (Titanic, Tips) to apply skills

## Tips for Success

- Develop a consistent EDA checklist
- Always visualize before and after transformations
- Document assumptions and decisions
- Create reusable functions for common operations
- When analyzing groups, always check sample sizes
