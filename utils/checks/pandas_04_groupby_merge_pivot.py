from utils.checker import check
import numpy as np
import pandas as pd

def p1(dept_salary):
    check.is_type(dept_salary, pd.Series, "P1: Type check")
    check.is_true(abs(dept_salary['HR'] - 57500.0) < 0.1, "P1: HR salary", "HR mean should be 57500")

def p2(dept_count):
    check.is_type(dept_count, pd.Series, "P2: Type check")
    check.is_true(dept_count['IT'] == 3, "P2: IT count", "IT should have 3 employees")
    check.is_true(dept_count['Sales'] == 1, "P2: Sales count", "Sales should have 1 employee")

def p3(concat_v):
    check.is_type(concat_v, pd.DataFrame, "P3: Type check")
    check.has_length(concat_v, 4, "P3: Length")
    check.has_columns(concat_v, ['A', 'B'], "P3: Columns")

def p4(concat_h):
    check.is_type(concat_h, pd.DataFrame, "P4: Type check")
    check.is_true(len(concat_h.columns) == 4, "P4: Four columns", "Should have 4 columns")
    check.has_columns(concat_h, ['A', 'B', 'C', 'D'], "P4: Columns")

def p5(merged):
    check.is_type(merged, pd.DataFrame, "P5: Type check")
    check.has_length(merged, 2, "P5: Length")
    check.contains_column(merged, 'salary', "P5: Has salary column")

def p6(dept_agg):
    check.is_type(dept_agg, pd.DataFrame, "P6: Type check")
    check.is_true(len(dept_agg.columns) == 2, "P6: Two columns", "Should have 2 aggregation columns")

def p7(left_merged):
    check.is_type(left_merged, pd.DataFrame, "P7: Type check")
    check.has_length(left_merged, 3, "P7: Length")
    check.is_true(pd.isna(left_merged[left_merged['name'] == 'Charlie']['salary'].iloc[0]), "P7: Charlie has NaN", "Charlie should have NaN salary")

def p8(df_with_avg):
    check.is_type(df_with_avg, pd.DataFrame, "P8: Type check")
    check.contains_column(df_with_avg, 'dept_avg_salary', "P8: Has dept_avg_salary column")
    check.has_length(df_with_avg, 6, "P8: Length")

def p9(dept_counts):
    check.is_type(dept_counts, pd.Series, "P9: Type check")
    check.is_true(dept_counts['IT'] == 3, "P9: IT count", "IT should have 3 occurrences")

def p10(pivot):
    check.is_type(pivot, pd.DataFrame, "P10: Type check")
    check.is_true(abs(pivot.loc['IT', 'salary'] - 55000.0) < 100, "P10: IT salary", "IT salary should be around 55000")

def p11(grouped_multi):
    check.is_type(grouped_multi, pd.Series, "P11: Type check")
    check.is_true(len(grouped_multi) >= 3, "P11: Multiple groups", "Should have at least 3 groups")

def p12(outer_merged):
    check.is_type(outer_merged, pd.DataFrame, "P12: Type check")
    check.has_length(outer_merged, 4, "P12: Length")

def p13(crosstab):
    check.is_type(crosstab, pd.DataFrame, "P13: Type check")
    check.is_true(crosstab.sum().sum() == 6, "P13: Total count", "Total should be 6")

def p14(melted):
    check.is_type(melted, pd.DataFrame, "P14: Type check")
    check.has_length(melted, 6, "P14: Length")
    check.contains_column(melted, 'value', "P14: Has value column")

def p15(salary_range):
    check.is_type(salary_range, pd.Series, "P15: Type check")
    check.is_true(salary_range['IT'] == 25000, "P15: IT range", "IT range should be 25000")
    check.is_true(salary_range['Sales'] == 0, "P15: Sales range", "Sales range should be 0")
