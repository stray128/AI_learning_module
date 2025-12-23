# Module 5: Statistics & Scikit-Learn Preprocessing

Bridge the gap between raw data and machine learning with statistical analysis and data preprocessing.

## What You'll Learn

This module covers essential statistical concepts and sklearn's preprocessing tools - the critical steps that prepare your data for modeling.

## Notebooks

### 1. Descriptive Statistics (`01_descriptive_stats.ipynb`)
**Problems:** 18 | **Difficulty:** Easy to Medium

Understand and summarize your data quantitatively:
- Measures of central tendency (mean, median, mode)
- Measures of spread (variance, standard deviation, range)
- Percentiles and quartiles
- Skewness and kurtosis
- Correlation and covariance
- Statistical testing basics

**Practical Application:** Generate summary statistics for reports, identify data characteristics, and validate assumptions.

---

### 2. Data Preprocessing (`02_preprocessing.ipynb`)
**Problems:** 17 | **Difficulty:** Easy to Hard

Transform features for optimal model performance:
- **StandardScaler:** Z-score normalization (mean=0, std=1)
- **MinMaxScaler:** Scale to [0,1] range
- **RobustScaler:** Scaling robust to outliers
- **Normalizer:** L1/L2 normalization per sample
- **SimpleImputer:** Handle missing values
- Inverse transforms to recover original scale

**Practical Application:** Prepare features for algorithms sensitive to scale (SVM, KNN, neural networks).

---

### 3. Encoding & Data Splitting (`03_encoding_splitting.ipynb`)
**Problems:** 16 | **Difficulty:** Medium to Hard

Convert categories and split data properly:
- **LabelEncoder:** Convert labels to integers
- **OneHotEncoder:** Create binary columns for categories
- **OrdinalEncoder:** Encode ordered categories
- **train_test_split:** Split data for validation
- **Stratified splitting:** Maintain class distribution
- **K-Fold cross-validation:** Robust model evaluation
- Handling unknown categories in test data

**Practical Application:** Prepare categorical features for ML models and set up proper train/test splits to avoid data leakage.

---

## Prerequisites

- Completion of Modules 2-3 (NumPy and Pandas)
- Basic understanding of statistics (mean, standard deviation)

## Key Preprocessing Decisions

| Situation | Recommended Scaler |
|-----------|-------------------|
| Data is normally distributed | StandardScaler |
| Need bounded range [0,1] | MinMaxScaler |
| Data has outliers | RobustScaler |
| Sparse data | MaxAbsScaler |
| Compare sample similarity | Normalizer |

## Critical Concept: Fit on Train, Transform on Both

```python
# CORRECT - prevents data leakage
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# WRONG - leaks test information into training
scaler.fit(X)  # Never fit on full dataset!
```

## Getting Started

1. Open `01_descriptive_stats.ipynb`
2. Complete notebooks in order
3. Pay special attention to the train/test splitting rules
4. Practice with both synthetic and real datasets

## Tips for Success

- Always split data BEFORE preprocessing
- Fit preprocessors only on training data
- Save fitted preprocessors for use on new data
- For categories in test but not train, use `handle_unknown='ignore'`
- Document your preprocessing pipeline for reproducibility
