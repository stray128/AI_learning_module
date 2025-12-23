# Module 3: Pandas for Data Analysis

Master the most important library for data manipulation and analysis in Python.

## What You'll Learn

Pandas provides intuitive data structures (Series and DataFrame) that make data manipulation feel natural. This module takes you from basics to advanced data wrangling techniques.

## Notebooks

### 1. Series & DataFrames (`01_series_dataframes.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Medium

Understand Pandas' core data structures:
- Creating Series from lists, dicts, and arrays
- Building DataFrames from various sources
- Accessing data with labels and positions
- Understanding index objects
- Basic DataFrame properties (shape, dtypes, info)
- Reading data from CSV files

**Practical Application:** Load datasets, explore their structure, and prepare them for analysis.

---

### 2. Selection & Filtering (`02_selection_filtering.ipynb`)
**Problems:** 20 | **Difficulty:** Easy to Hard

Extract exactly the data you need:
- Selecting columns by name
- Row selection with `loc` (label-based) and `iloc` (position-based)
- Boolean filtering with conditions
- Combining multiple conditions (AND, OR, NOT)
- Using `isin()` for multiple value matching
- Query strings for readable filtering

**Practical Application:** Filter customer data by criteria, extract date ranges, and create analysis subsets.

---

### 3. Data Cleaning (`03_data_cleaning.ipynb`)
**Problems:** 20 | **Difficulty:** Medium to Hard

Handle real-world messy data:
- Detecting and handling missing values (`NaN`)
- Filling missing values (mean, median, forward/backward fill)
- Dropping rows or columns with missing data
- Handling duplicates
- Data type conversion
- String cleaning and manipulation
- Renaming columns

**Practical Application:** Prepare raw data for analysis by handling the inconsistencies found in real datasets.

---

### 4. GroupBy, Merge & Pivot (`04_groupby_merge_pivot.ipynb`)
**Problems:** 20 | **Difficulty:** Medium to Hard

Perform powerful aggregations and combine datasets:
- GroupBy operations for split-apply-combine workflows
- Multiple aggregation functions
- Merging DataFrames (inner, outer, left, right joins)
- Concatenating DataFrames
- Pivot tables and cross-tabulation
- Melting (unpivoting) data

**Practical Application:** Generate summary reports, combine data from multiple sources, and reshape data for visualization or modeling.

---

## Prerequisites

- Completion of Module 2 (NumPy) strongly recommended
- Understanding of tabular data (rows and columns)
- Basic SQL knowledge helpful but not required

## Key Concepts

| Concept | Description |
|---------|-------------|
| DataFrame | 2D labeled data structure (like a spreadsheet or SQL table) |
| Series | 1D labeled array (a single column) |
| Index | Labels for rows/columns that enable fast lookup |
| `loc` vs `iloc` | Label-based vs position-based selection |
| GroupBy | Split data into groups, apply function, combine results |

## Getting Started

1. Open `01_series_dataframes.ipynb`
2. Run the setup cell
3. Complete notebooks in order - concepts build progressively
4. Practice with the provided datasets

## Tips for Success

- Use `.head()` and `.tail()` to preview data
- Check data types with `.dtypes` before operations
- Use `.info()` for a quick dataset overview
- When merging, always verify the result shape makes sense
- Remember: most Pandas operations return a new object (not in-place)
