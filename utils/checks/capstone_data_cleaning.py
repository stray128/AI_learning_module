"""
Verification functions for Capstone Project 2: Real-World Data Cleaning Challenge
"""

from utils.checker import check
import numpy as np
import pandas as pd


def p0(g, messy_df):
    """Verify library imports and dataset loaded"""
    check.is_true('np' in g, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in g, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('plt' in g, "P0c: Matplotlib imported", "Import matplotlib.pyplot as plt")
    check.is_true('os' in g, "P0d: OS module imported", "Import os module")
    check.is_true('messy_df' in g, "P0e: Dataset loaded", "Load the messy dataset into messy_df")


def p1(missing_summary):
    """Verify missing data assessment"""
    check.is_type(missing_summary, pd.DataFrame, "P1: Type check")
    check.contains_column(missing_summary, 'missing_count', "P1: Has missing_count column")
    check.contains_column(missing_summary, 'missing_pct', "P1: Has missing_pct column")


def p2(current_dtypes, df):
    """Verify data types examination"""
    check.is_type(current_dtypes, pd.Series, "P2: Type check")
    check.has_length(current_dtypes, len(df.columns), "P2: Has entry for each column")


def p3(duplicates_removed, df):
    """Verify duplicate rows removed"""
    check.is_type(duplicates_removed, (int, np.integer), "P3: Type check")
    check.is_true(df.duplicated().sum() == 0, "P3: No duplicates remain", "All duplicates should be removed")


def p4(string_cols_cleaned):
    """Verify string columns cleaned"""
    check.is_type(string_cols_cleaned, (int, np.integer), "P4: Type check")
    check.is_true(string_cols_cleaned > 0, "P4: At least one string column", "Should have cleaned at least one string column")


def p5(numeric_cols_converted):
    """Verify numeric columns converted"""
    check.is_type(numeric_cols_converted, (int, np.integer), "P5: Type check")
    check.is_true(numeric_cols_converted >= 0, "P5: Non-negative count", "Should be a non-negative number")


def p6(values_filled, df):
    """Verify missing numeric values filled"""
    check.is_type(values_filled, (int, np.integer), "P6: Type check")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    numeric_missing = df[numeric_cols].isnull().sum().sum()
    check.is_true(numeric_missing == 0, "P6: No missing numeric values", "All numeric missing values should be filled")


def p7(cat_filled, df):
    """Verify missing categorical values filled"""
    check.is_type(cat_filled, (int, np.integer), "P7: Type check")
    total_missing = df.isnull().sum().sum()
    check.is_true(total_missing == 0, "P7: No missing values", "All missing values should be filled")


def p8(outlier_counts):
    """Verify outliers detected using IQR"""
    check.is_type(outlier_counts, dict, "P8: Type check")
    check.is_true(len(outlier_counts) > 0, "P8: Has entries", "Should have outlier counts for numeric columns")


def p9(values_capped):
    """Verify outliers handled with winsorization"""
    check.is_type(values_capped, (int, np.integer), "P9: Type check")
    check.is_true(values_capped >= 0, "P9: Non-negative count", "Should be a non-negative number")


def p10(unique_before, unique_after):
    """Verify category values standardized"""
    check.is_type(unique_before, dict, "P10a: unique_before is dict")
    check.is_type(unique_after, dict, "P10b: unique_after is dict")


def p11(cleaning_report):
    """Verify data cleaning report created"""
    check.is_type(cleaning_report, dict, "P11: Type check")
    check.contains(cleaning_report.keys(), 'original_rows', "P11a: Has original_rows")
    check.contains(cleaning_report.keys(), 'final_missing_pct', "P11b: Has final_missing_pct")
    check.is_true(cleaning_report.get('final_missing_pct', -1) == 0.0, "P11c: No missing values", "final_missing_pct should be 0.0")


def p12(final_dtypes, df):
    """Verify final data types validated"""
    check.is_type(final_dtypes, pd.Series, "P12: Type check")
    check.has_length(final_dtypes, len(df.columns), "P12: Has entry for each column")


def p13(axes):
    """Verify data quality improvement visualization"""
    check.is_not_none(axes, "P13: Axes created")
    check.has_length(axes, 2, "P13: Has 2 subplots")


def p14(save_success):
    """Verify cleaned data saved"""
    check.is_type(save_success, bool, "P14: Type check")
    check.is_true(save_success == True, "P14: File saved", "File should be saved successfully")


def p15(final_summary):
    """Verify final summary created"""
    check.is_type(final_summary, dict, "P15: Type check")
    check.contains(final_summary.keys(), 'shape', "P15a: Has shape")
    check.contains(final_summary.keys(), 'missing_values', "P15b: Has missing_values")
    check.is_true(final_summary.get('missing_values', -1) == 0, "P15c: No missing values", "missing_values should be 0")
