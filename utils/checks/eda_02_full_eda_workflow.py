from utils.checker import check
import numpy as np
import pandas as pd


def p0(g):
    """Check Problem 0: Import Libraries and Load Data"""
    check.is_true('np' in g, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in g, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('plt' in g, "P0c: Matplotlib imported", "Import matplotlib.pyplot as plt")
    check.is_true('titanic' in g, "P0d: Titanic loaded", "Load titanic dataset using pd.read_csv(TITANIC_PATH)")
    check.is_true('tips' in g, "P0e: Tips loaded", "Load tips dataset using pd.read_csv(TIPS_PATH)")


def p1(shape):
    """Check Problem 1: Get Dataset Shape"""
    check.is_not_none(shape, "P1: Not None")
    check.is_type(shape, tuple, "P1: Type check")
    check.has_length(shape, 2, "P1: Tuple length")
    check.is_true(shape[0] > 0, "P1: Has rows", "Dataset should have at least one row")


def p2(dtypes):
    """Check Problem 2: Get Data Types"""
    check.is_not_none(dtypes, "P2: Not None")
    check.is_type(dtypes, pd.Series, "P2: Type check")
    check.is_true(len(dtypes) > 0, "P2: Has entries", "Should have data types for all columns")


def p3(first_rows, last_rows, titanic):
    """Check Problem 3: Preview First Rows"""
    check.is_not_none(first_rows, "P3: first_rows not None")
    check.is_not_none(last_rows, "P3: last_rows not None")
    check.is_type(first_rows, pd.DataFrame, "P3: first_rows type")
    check.is_type(last_rows, pd.DataFrame, "P3: last_rows type")
    check.has_shape(first_rows, (3, titanic.shape[1]), "P3: first_rows shape")
    check.has_shape(last_rows, (3, titanic.shape[1]), "P3: last_rows shape")


def p4(missing_counts, titanic):
    """Check Problem 4: Count Missing Values"""
    check.is_not_none(missing_counts, "P4: Not None")
    check.is_type(missing_counts, pd.Series, "P4: Type check")
    check.is_true(all(missing_counts >= 0), "P4: Non-negative counts", "Counts should be non-negative")
    check.has_length(missing_counts, titanic.shape[1], "P4: Length matches columns")


def p5(missing_pct, titanic):
    """Check Problem 5: Calculate Missing Percentage"""
    check.is_not_none(missing_pct, "P5: Not None")
    check.is_type(missing_pct, pd.Series, "P5: Type check")
    check.all_values_in_range(missing_pct, 0, 100, "P5: Percentage range")
    check.has_length(missing_pct, titanic.shape[1], "P5: Length matches columns")


def p6(desc_stats):
    """Check Problem 6: Get Descriptive Statistics"""
    check.is_not_none(desc_stats, "P6: Not None")
    check.is_type(desc_stats, pd.DataFrame, "P6: Type check")
    check.contains(list(desc_stats.index), 'mean', "P6: Contains mean")
    check.contains(list(desc_stats.index), 'std', "P6: Contains std")


def p7(day_counts):
    """Check Problem 7: Value Counts for Categorical Column"""
    check.is_not_none(day_counts, "P7: Not None")
    check.is_type(day_counts, pd.Series, "P7: Type check")
    check.is_true(len(day_counts) > 0, "P7: Has entries", "Should have at least one entry")
    check.is_true(all(day_counts > 0), "P7: Positive counts", "All counts should be positive")


def p8(unique_vals, n_unique):
    """Check Problem 8: Count Unique Values"""
    check.is_not_none(unique_vals, "P8: unique_vals not None")
    check.is_not_none(n_unique, "P8: n_unique not None")
    check.is_type(unique_vals, np.ndarray, "P8: unique_vals type")
    check.is_type(n_unique, (int, np.integer), "P8: n_unique type")
    check.is_true(n_unique == len(unique_vals), "P8: Counts match", "n_unique should equal length of unique_vals")


def p9(n, bins, patches):
    """Check Problem 9: Create Histogram"""
    check.is_not_none(n, "P9: n not None")
    check.is_not_none(bins, "P9: bins not None")
    check.is_not_none(patches, "P9: patches not None")
    check.is_type(n, np.ndarray, "P9: n is array")


def p10(bp):
    """Check Problem 10: Create Box Plot by Category"""
    check.is_not_none(bp, "P10: Not None")


def p11(scatter1, scatter2):
    """Check Problem 11: Create Scatter Plot with Groups"""
    check.is_not_none(scatter1, "P11: scatter1 not None")
    check.is_not_none(scatter2, "P11: scatter2 not None")


def p12(grouped_mean):
    """Check Problem 12: Group Statistics"""
    check.is_not_none(grouped_mean, "P12: Not None")
    check.is_type(grouped_mean, pd.Series, "P12: Type check")
    check.is_true(isinstance(grouped_mean.index, pd.MultiIndex), "P12: MultiIndex", "Should have MultiIndex from grouping by two columns")


def p13(bars):
    """Check Problem 13: Create Bar Chart of Aggregated Data"""
    check.is_not_none(bars, "P13: Not None")


def p14(wedges):
    """Check Problem 14: Create Pie Chart"""
    check.is_not_none(wedges, "P14: Not None")


def p15(tips_with_pct):
    """Check Problem 15: Create Derived Feature"""
    check.contains_column(tips_with_pct, 'tip_percentage', "P15: Column exists")
    check.all_values_in_range(tips_with_pct['tip_percentage'], 0, 100, "P15: Percentage range")
    check.is_true(10 < tips_with_pct['tip_percentage'].mean() < 20, "P15: Reasonable mean", "Mean tip percentage should be between 10 and 20")


def p16(axes):
    """Check Problem 16: Create Multi-Panel Figure"""
    check.is_true(axes.shape == (2, 2), "P16: Axes shape", "Should have 2x2 grid of subplots")


def p17(summary_table):
    """Check Problem 17: Multi-Group Summary Statistics"""
    check.is_not_none(summary_table, "P17: Not None")
    check.is_type(summary_table, pd.DataFrame, "P17: Type check")
    check.contains(list(summary_table.columns), 'mean', "P17: Has mean column")
    check.contains(list(summary_table.columns), 'std', "P17: Has std column")


def p18(weekend_dinner, stats, tips):
    """Check Problem 18: Filter and Analyze Subset"""
    check.is_not_none(weekend_dinner, "P18: weekend_dinner not None")
    check.is_not_none(stats, "P18: stats not None")
    check.is_type(weekend_dinner, pd.DataFrame, "P18: weekend_dinner type")
    check.is_type(stats, pd.DataFrame, "P18: stats type")
    check.is_true(len(weekend_dinner) > 0, "P18: Has rows", "Should have at least one row")
    check.is_true(len(weekend_dinner) < len(tips), "P18: Filtered subset", "Should have fewer rows than original")


def p19(high_tippers, tips):
    """Check Problem 19: Identify High Values"""
    check.is_not_none(high_tippers, "P19: Not None")
    check.is_type(high_tippers, pd.DataFrame, "P19: Type check")
    check.is_true(len(high_tippers) > 0, "P19: Has rows", "Should have at least one high tipper")
    check.is_true(len(high_tippers) < len(tips), "P19: Subset", "Should be a subset of original data")


def p20(eda_report):
    """Check Problem 20: Create EDA Report Function"""
    check.is_not_none(eda_report, "P20: Report not None")
    check.is_type(eda_report, dict, "P20: Type check")
    check.is_not_none(eda_report['shape'], "P20: Shape populated")
    check.is_not_none(eda_report['columns'], "P20: Columns populated")
    check.is_not_none(eda_report['dtypes'], "P20: Dtypes populated")
    check.is_not_none(eda_report['missing_counts'], "P20: Missing counts populated")
    check.is_not_none(eda_report['missing_pct'], "P20: Missing pct populated")
    check.is_not_none(eda_report['numerical_stats'], "P20: Stats populated")
    check.is_not_none(eda_report['categorical_columns'], "P20: Categorical columns populated")
