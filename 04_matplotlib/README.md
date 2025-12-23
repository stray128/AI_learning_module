# Module 4: Data Visualization with Matplotlib

Transform data into compelling visual stories that drive insights and decisions.

## What You'll Learn

Matplotlib is Python's foundational plotting library. Master it, and you'll be able to create any visualization you can imagine - from simple line charts to complex multi-panel dashboards.

## Notebooks

### 1. Basic Plots (`01_basic_plots.ipynb`)
**Problems:** 15 | **Difficulty:** Easy to Medium

Create fundamental chart types:
- Line plots for trends over time
- Scatter plots for relationships between variables
- Bar charts for categorical comparisons
- Setting titles, labels, and legends
- Customizing colors and line styles
- Saving figures to files

**Practical Application:** Create standard business charts, visualize time series data, and compare categories.

---

### 2. Histograms & Distributions (`02_histograms_distributions.ipynb`)
**Problems:** 15 | **Difficulty:** Easy to Medium

Visualize data distributions:
- Histograms for frequency distributions
- Controlling bin sizes and ranges
- Density plots and KDE
- Box plots for quartiles and outliers
- Violin plots for distribution shape
- Comparing distributions across groups

**Practical Application:** Understand data spread, identify outliers, and validate statistical assumptions.

---

### 3. Subplots & Customization (`03_subplots_customization.ipynb`)
**Problems:** 15 | **Difficulty:** Medium to Hard

Create professional multi-panel figures:
- Creating subplot grids with `plt.subplots()`
- Sharing axes across subplots
- Adjusting figure size and layout
- Customizing tick marks and grid lines
- Adding annotations and text
- Using different scales (log, symlog)
- Creating publication-ready figures

**Practical Application:** Build dashboards, create comparison panels, and produce figures for reports and presentations.

---

## Prerequisites

- Completion of Modules 2-3 (NumPy and Pandas)
- Understanding of data types suitable for different chart types

## Chart Selection Guide

| Data Type | Best Chart |
|-----------|------------|
| Trend over time | Line plot |
| Relationship between 2 variables | Scatter plot |
| Comparing categories | Bar chart |
| Distribution of values | Histogram or box plot |
| Part of whole | Pie chart (use sparingly) |
| Multiple distributions | Violin or overlaid histograms |

## Getting Started

1. Open `01_basic_plots.ipynb`
2. Run `%matplotlib inline` to display plots in the notebook
3. Experiment with parameters to understand their effects
4. Focus on readability - good labels make good charts

## Tips for Success

- Always label your axes and add a title
- Choose colors that are colorblind-friendly
- Use `plt.tight_layout()` to prevent overlapping elements
- Start simple, then add complexity
- When in doubt, use `fig, ax = plt.subplots()` for more control

## Common Patterns

```python
# Basic pattern for all plots
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)  # or ax.bar(), ax.scatter(), etc.
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Chart Title')
plt.show()
```
