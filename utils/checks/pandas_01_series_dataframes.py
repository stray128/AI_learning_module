from utils.checker import check
import numpy as np
import pandas as pd

def p1(series):
    check.is_type(series, pd.Series, "P1: Type check")
    check.has_length(series, 5, "P1: Length")
    check.first_element_is(series, 10, "P1: First element")

def p2(indexed_series):
    check.is_type(indexed_series, pd.Series, "P2: Type check")
    check.has_index(indexed_series, ['a', 'b', 'c'], "P2: Index")
    check.element_at_is(indexed_series, 'a', 100, "P2: Value at 'a'")

def p3(df):
    check.is_type(df, pd.DataFrame, "P3: Type check")
    check.has_shape(df, (3, 3), "P3: Shape")
    check.has_columns(df, ['name', 'age', 'city'], "P3: Columns")

def p4(df_shape):
    check.is_type(df_shape, tuple, "P4: Type check")
    check.is_true(df_shape == (3, 3), "P4: Correct shape", "Shape should be (3, 3)")

def p5(columns):
    check.is_type(columns, list, "P5: Type check")
    check.is_true(columns == ['name', 'age', 'city'], "P5: Correct columns", "Should be ['name', 'age', 'city']")

def p6(titanic):
    check.is_type(titanic, pd.DataFrame, "P6: Type check")
    check.is_true(len(titanic) > 0, "P6: Not empty", "DataFrame should have rows")
    check.is_true(len(titanic.columns) > 0, "P6: Has columns", "DataFrame should have columns")

def p7(dtypes, titanic):
    check.is_type(dtypes, pd.Series, "P7: Type check")
    check.is_true(len(dtypes) == len(titanic.columns), "P7: Length matches columns", "Should have dtype for each column")

def p8(head_5, titanic):
    check.is_type(head_5, pd.DataFrame, "P8: Type check")
    check.has_length(head_5, 5, "P8: Length")
    check.is_true(list(head_5.columns) == list(titanic.columns), "P8: Same columns", "Should have same columns as titanic")

def p9(stats):
    check.is_type(stats, pd.DataFrame, "P9: Type check")
    check.contains(list(stats.index), 'mean', "P9: Contains 'mean'")
    check.contains(list(stats.index), 'std', "P9: Contains 'std'")

def p10(ages):
    check.is_type(ages, pd.Series, "P10: Type check")
    check.has_length(ages, 3, "P10: Length")
    check.is_true(list(ages) == [25, 30, 35], "P10: Correct values", "Values should be [25, 30, 35]")

def p11(custom_df):
    check.has_columns(custom_df, ['A', 'B', 'C'], "P11: Columns")
    check.has_index(custom_df, ['row1', 'row2', 'row3'], "P11: Index")
    check.has_shape(custom_df, (3, 3), "P11: Shape")

def p12(df_renamed, df):
    check.has_columns(df_renamed, ['Name', 'Age', 'City'], "P12: Columns")
    check.has_shape(df_renamed, (3, 3), "P12: Shape")
    check.is_true(list(df.columns) == ['name', 'age', 'city'], "P12: Original unchanged", "Original df should not be modified")

def p13(df_indexed):
    check.has_index(df_indexed, ['Alice', 'Bob', 'Charlie'], "P13: Index")
    check.not_contains(list(df_indexed.columns), 'name', "P13: 'name' not in columns")
    check.is_true(len(df_indexed.columns) == 2, "P13: Two columns remain", "Should have 2 columns after setting index")

def p14(df_with_country):
    check.contains_column(df_with_country, 'country', "P14: Has 'country' column")
    check.is_true(all(df_with_country['country'] == 'USA'), "P14: All values are 'USA'", "All country values should be 'USA'")
    check.is_true(len(df_with_country.columns) == 4, "P14: Four columns", "Should have 4 columns")

def p15(np_df):
    check.has_shape(np_df, (4, 3), "P15: Shape")
    check.has_columns(np_df, ['X', 'Y', 'Z'], "P15: Columns")
    check.has_index(np_df, ['a', 'b', 'c', 'd'], "P15: Index")
