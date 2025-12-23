from utils.checker import check
import numpy as np
import pandas as pd

def p1(missing_mask, df):
    check.is_type(missing_mask, pd.DataFrame, "P1: Type check")
    check.has_shape(missing_mask, df.shape, "P1: Shape")
    check.is_true(missing_mask.iloc[2]['name'] == True, "P1: Name missing at row 2", "Row 2 name should be missing")

def p2(missing_counts):
    check.is_type(missing_counts, pd.Series, "P2: Type check")
    check.is_true(missing_counts['age'] == 2, "P2: Age missing count", "Age should have 2 missing values")

def p3(df_clean):
    check.is_type(df_clean, pd.DataFrame, "P3: Type check")
    check.has_length(df_clean, 2, "P3: Length")
    check.has_no_nulls(df_clean, "P3: No nulls")

def p4(age_filled):
    check.is_type(age_filled, pd.Series, "P4: Type check")
    check.has_no_nulls(age_filled, "P4: No nulls")
    check.is_true(age_filled.iloc[1] == 0, "P4: Filled with 0", "Index 1 should be 0")

def p5(age_int):
    check.is_type(age_int, pd.Series, "P5: Type check")
    check.has_dtype(age_int, np.int64, "P5: Dtype")

def p6(salary_filled):
    check.is_type(salary_filled, pd.Series, "P6: Type check")
    check.has_no_nulls(salary_filled, "P6: No nulls")
    check.is_true(abs(salary_filled.iloc[2] - 52500.0) < 1, "P6: Mean value", "Should be filled with mean")

def p7(df_cols_clean):
    check.is_type(df_cols_clean, pd.DataFrame, "P7: Type check")
    check.is_true(len(df_cols_clean.columns) == 0, "P7: No columns", "All columns have missing values")

def p8(is_dup):
    check.is_type(is_dup, pd.Series, "P8: Type check")
    check.is_true(is_dup.sum() == 1, "P8: One duplicate", "Should have 1 duplicate row")

def p9(df_no_dup):
    check.is_type(df_no_dup, pd.DataFrame, "P9: Type check")
    check.has_length(df_no_dup, 3, "P9: Length")

def p10(dept_upper):
    check.is_type(dept_upper, pd.Series, "P10: Type check")
    check.is_true(dept_upper.iloc[0] == 'IT', "P10: First element", "First element should be 'IT'")

def p11(age_ffill):
    check.is_type(age_ffill, pd.Series, "P11: Type check")
    check.is_true(age_ffill.iloc[1] == 25.0, "P11: Index 1", "Should be forward filled to 25.0")
    check.is_true(age_ffill.iloc[4] == 28.0, "P11: Index 4", "Should be forward filled to 28.0")

def p12(dept_replaced):
    check.is_type(dept_replaced, pd.Series, "P12: Type check")
    check.is_true(dept_replaced.iloc[0] == 'Technology', "P12: Index 0", "Should be 'Technology'")
    check.is_true(dept_replaced.iloc[2] == 'Technology', "P12: Index 2", "Should be 'Technology'")

def p13(df_thresh):
    check.is_type(df_thresh, pd.DataFrame, "P13: Type check")
    check.has_length(df_thresh, 4, "P13: Length")

def p14(df_filled):
    check.is_type(df_filled, pd.DataFrame, "P14: Type check")
    check.has_no_nulls(df_filled, "P14: No nulls")
    check.is_true(df_filled['name'].iloc[2] == 'Unknown', "P14: Name filled", "Should be 'Unknown'")
    check.is_true(df_filled['dept'].iloc[3] == 'Other', "P14: Dept filled", "Should be 'Other'")

def p15(s_interp):
    check.is_type(s_interp, pd.Series, "P15: Type check")
    check.is_true(abs(s_interp.iloc[1] - 2.0) < 0.1, "P15: Index 1", "Should be approximately 2.0")
    check.is_true(abs(s_interp.iloc[2] - 3.0) < 0.1, "P15: Index 2", "Should be approximately 3.0")
