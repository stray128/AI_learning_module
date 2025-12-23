from utils.checker import check
import numpy as np
import pandas as pd

def p1(names):
    check.is_type(names, pd.Series, "P1: Type check")
    check.has_length(names, 5, "P1: Length")
    check.first_element_is(names, 'Alice', "P1: First element")

def p2(name_age):
    check.is_type(name_age, pd.DataFrame, "P2: Type check")
    check.has_columns(name_age, ['name', 'age'], "P2: Columns")
    check.is_true(len(name_age.columns) == 2, "P2: Two columns", "Should have exactly 2 columns")

def p3(first_row):
    check.is_type(first_row, pd.Series, "P3: Type check")
    check.is_true(first_row['name'] == 'Alice', "P3: First row name", "Name should be 'Alice'")

def p4(rows_1_to_3):
    check.is_type(rows_1_to_3, pd.DataFrame, "P4: Type check")
    check.has_length(rows_1_to_3, 2, "P4: Length")
    check.is_true(rows_1_to_3.iloc[0]['name'] == 'Bob', "P4: First row", "First row should be 'Bob'")

def p5(value):
    check.is_type(value, (int, np.integer), "P5: Type check")
    check.is_true(value == 35, "P5: Correct value", "Value should be 35")

def p6(older_than_25):
    check.is_type(older_than_25, pd.DataFrame, "P6: Type check")
    check.has_length(older_than_25, 3, "P6: Length")
    check.is_true(all(older_than_25['age'] > 25), "P6: All ages > 25", "All ages should be greater than 25")

def p7(it_dept):
    check.is_type(it_dept, pd.DataFrame, "P7: Type check")
    check.has_length(it_dept, 2, "P7: Length")
    check.is_true(all(it_dept['dept'] == 'IT'), "P7: All IT dept", "All rows should have dept='IT'")

def p8(bob_row):
    check.is_type(bob_row, pd.Series, "P8: Type check")
    check.is_true(bob_row['age'] == 30, "P8: Bob's age", "Age should be 30")

def p9(subset):
    check.is_type(subset, pd.DataFrame, "P9: Type check")
    check.has_shape(subset, (2, 2), "P9: Shape")
    check.has_columns(subset, ['age', 'salary'], "P9: Columns")

def p10(it_hr):
    check.is_type(it_hr, pd.DataFrame, "P10: Type check")
    check.has_length(it_hr, 4, "P10: Length")
    check.is_true(all(it_hr['dept'].isin(['IT', 'HR'])), "P10: IT or HR", "All depts should be 'IT' or 'HR'")

def p11(filtered):
    check.is_type(filtered, pd.DataFrame, "P11: Type check")
    check.has_length(filtered, 3, "P11: Length")
    check.is_true(all((filtered['age'] > 25) & (filtered['salary'] > 50000)), "P11: Both conditions", "All rows should satisfy both conditions")

def p12(or_filtered):
    check.is_type(or_filtered, pd.DataFrame, "P12: Type check")
    check.has_length(or_filtered, 2, "P12: Length")
    check.is_true(all((or_filtered['age'] < 25) | (or_filtered['salary'] > 65000)), "P12: At least one condition", "All rows should satisfy at least one condition")

def p13(query_result):
    check.is_type(query_result, pd.DataFrame, "P13: Type check")
    check.has_length(query_result, 1, "P13: Length")
    check.is_true(query_result.iloc[0]['name'] == 'Charlie', "P13: Charlie", "Result should be Charlie")

def p14(names_salaries):
    check.is_type(names_salaries, pd.DataFrame, "P14: Type check")
    check.has_columns(names_salaries, ['name', 'salary'], "P14: Columns")
    check.has_length(names_salaries, 3, "P14: Length")

def p15(not_it):
    check.is_type(not_it, pd.DataFrame, "P15: Type check")
    check.has_length(not_it, 3, "P15: Length")
    check.is_true(all(not_it['dept'] != 'IT'), "P15: No IT dept", "No rows should have dept='IT'")
