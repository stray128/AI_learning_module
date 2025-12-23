from utils.checker import check
import numpy as np
import pandas as pd


def p0(g):
    """Check Problem 0: Import Required Libraries"""
    check.is_true('np' in g, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in g, "P0b: Pandas imported", "Import pandas as pd")


def p1(arr):
    """Check Problem 1: DataFrame to NumPy Array"""
    check.is_not_none(arr, "P1: Not None")
    check.is_type(arr, np.ndarray, "P1: Type check")
    check.has_shape(arr, (3, 2), "P1: Shape check")


def p2(df):
    """Check Problem 2: NumPy Array to DataFrame"""
    check.is_not_none(df, "P2: Not None")
    check.is_type(df, pd.DataFrame, "P2: Type check")
    check.has_columns(df, ['X', 'Y'], "P2: Column names")
    check.has_shape(df, (3, 2), "P2: Shape check")


def p3(sqrt_vals):
    """Check Problem 3: Apply NumPy Function to Column"""
    check.is_not_none(sqrt_vals, "P3: Not None")
    check.is_type(sqrt_vals, pd.Series, "P3: Type check")
    check.has_length(sqrt_vals, 5, "P3: Length check")
    check.first_element_is(sqrt_vals, 1.0, "P3: First element")
    check.last_element_is(sqrt_vals, 5.0, "P3: Last element")


def p4(df):
    """Check Problem 4: Use np.where with DataFrame"""
    check.contains_column(df, 'label', "P4: Column exists")
    check.is_type(df['label'], pd.Series, "P4: Type check")
    check.element_at_is(df['label'], 0, 'Low', "P4: First element")
    check.element_at_is(df['label'], 1, 'High', "P4: Second element")


def p5(arr):
    """Check Problem 5: Series to NumPy Array"""
    check.is_not_none(arr, "P5: Not None")
    check.is_type(arr, np.ndarray, "P5: Type check")
    check.has_length(arr, 5, "P5: Length check")
    check.first_element_is(arr, 10, "P5: First element")
    check.last_element_is(arr, 50, "P5: Last element")


def p6(df_added):
    """Check Problem 6: Apply NumPy Broadcasting"""
    check.is_not_none(df_added, "P6: Not None")
    check.is_type(df_added, pd.DataFrame, "P6: Type check")
    check.has_shape(df_added, (3, 2), "P6: Shape check")
    check.sum_is(df_added['A'], 36, "P6: Column A sum")
    check.sum_is(df_added['B'], 45, "P6: Column B sum")


def p7(df_clipped):
    """Check Problem 7: Use np.clip on DataFrame"""
    check.is_not_none(df_clipped, "P7: Not None")
    check.is_type(df_clipped, pd.DataFrame, "P7: Type check")
    check.min_value_is(df_clipped['values'], 20, "P7: Minimum value")
    check.max_value_is(df_clipped['values'], 80, "P7: Maximum value")


def p8(z_scores):
    """Check Problem 8: Calculate Z-Scores Using NumPy"""
    check.is_not_none(z_scores, "P8: Not None")
    check.is_type(z_scores, pd.Series, "P8: Type check")
    check.has_length(z_scores, 5, "P8: Length check")
    check.is_true(abs(z_scores.iloc[2]) < 0.01, "P8: Middle value z-score", "Middle value should have z-score near 0")


def p9(df_result):
    """Check Problem 9: Apply Custom NumPy Function"""
    check.is_not_none(df_result, "P9: Not None")
    check.is_type(df_result, pd.DataFrame, "P9: Type check")
    check.is_true(abs(df_result['A'].min() - 0.0) < 0.01, "P9: Column A min", "Min should be 0")
    check.is_true(abs(df_result['A'].max() - 1.0) < 0.01, "P9: Column A max", "Max should be 1")
    check.is_true(abs(df_result['B'].min() - 0.0) < 0.01, "P9: Column B min", "Min should be 0")


def p10(df_random):
    """Check Problem 10: NumPy Random Data in DataFrame"""
    check.is_not_none(df_random, "P10: Not None")
    check.is_type(df_random, pd.DataFrame, "P10: Type check")
    check.has_shape(df_random, (100, 2), "P10: Shape check")
    check.contains_column(df_random, 'normal', "P10: Has 'normal' column")
    check.contains_column(df_random, 'uniform', "P10: Has 'uniform' column")
    check.all_values_in_range(df_random['uniform'], 0, 1, "P10: Uniform range")


def p11(corr_matrix):
    """Check Problem 11: Correlation Matrix"""
    check.is_not_none(corr_matrix, "P11: Not None")
    check.is_type(corr_matrix, pd.DataFrame, "P11: Type check")
    check.is_true(abs(corr_matrix.loc['A', 'B'] - 1.0) < 0.01, "P11: A-B correlation", "A and B should have perfect positive correlation")
    check.is_true(abs(corr_matrix.loc['A', 'C'] - (-1.0)) < 0.01, "P11: A-C correlation", "A and C should have perfect negative correlation")


def p12(df):
    """Check Problem 12: Vectorized String Operations"""
    check.contains_column(df, 'name_clean', "P12: Column exists")
    check.is_true(df['name_clean'].iloc[0] == 'Alice', "P12: First name", "Should be 'Alice'")
    check.is_true(df['name_clean'].iloc[1] == 'Bob', "P12: Second name", "Should be 'Bob'")
    check.is_true(df['name_clean'].iloc[2] == 'Charlie', "P12: Third name", "Should be 'Charlie'")
    check.is_true(all(name == name.strip() for name in df['name_clean']), "P12: No whitespace", "Names should have no leading/trailing whitespace")


def p13(df):
    """Check Problem 13: Use np.select for Multiple Conditions"""
    check.contains_column(df, 'grade', "P13: Column exists")
    check.element_at_is(df['grade'], 0, 'F', "P13: First grade")
    check.element_at_is(df['grade'], 1, 'D', "P13: Second grade")
    check.element_at_is(df['grade'], 2, 'C', "P13: Third grade")
    check.element_at_is(df['grade'], 4, 'A', "P13: Fifth grade")


def p14(rolling_mean):
    """Check Problem 14: Rolling Window Calculations"""
    check.is_not_none(rolling_mean, "P14: Not None")
    check.is_type(rolling_mean, pd.Series, "P14: Type check")
    check.has_length(rolling_mean, 10, "P14: Length check")
    check.is_true(abs(rolling_mean.iloc[2] - 2.0) < 0.01, "P14: Third value", "Third value should be 2.0")


def p15(is_outlier):
    """Check Problem 15: Find Outliers with IQR Method"""
    check.is_not_none(is_outlier, "P15: Not None")
    check.is_type(is_outlier, pd.Series, "P15: Type check")
    check.sum_is(is_outlier, 1, "P15: Number of outliers")
    check.is_true(is_outlier.iloc[-1] == True, "P15: Last value is outlier", "The value 100 should be identified as outlier")


def p16(df):
    """Check Problem 16: Bin Data with pd.cut"""
    check.contains_column(df, 'age_group', "P16: Column exists")
    check.element_at_is(df['age_group'], 0, 'Child', "P16: First age group")
    check.element_at_is(df['age_group'], 7, 'Senior', "P16: Last age group")


def p17(df):
    """Check Problem 17: Cumulative Operations"""
    check.contains_column(df, 'cumsum', "P17: cumsum column exists")
    check.contains_column(df, 'cummax', "P17: cummax column exists")
    check.element_at_is(df['cumsum'], 0, 5, "P17: First cumsum")
    check.element_at_is(df['cumsum'], 4, 28, "P17: Last cumsum")
    check.element_at_is(df['cummax'], 4, 10, "P17: Last cummax")


def p18(df):
    """Check Problem 18: Rank Data"""
    check.contains_column(df, 'rank', "P18: Column exists")
    check.is_true(df[df['score'] == 92]['rank'].iloc[0] == 1.0, "P18: Highest score rank", "Score 92 should have rank 1")
    check.is_true(all(df['rank'] > 0), "P18: Positive ranks", "All ranks should be positive")


def p19(df):
    """Check Problem 19: Percentage Change"""
    check.contains_column(df, 'pct_change', "P19: Column exists")
    check.is_true(abs(df['pct_change'].iloc[1] - 0.10) < 0.01, "P19: Second value", "Should be approximately 0.10")
    check.is_true(pd.isna(df['pct_change'].iloc[0]), "P19: First value is NaN", "First value should be NaN")


def p20(df):
    """Check Problem 20: Complex Data Transformation"""
    check.contains_column(df, 'pct_of_product_total', "P20: Column exists")
    product_a_sum = df[df['product'] == 'A']['pct_of_product_total'].sum()
    product_b_sum = df[df['product'] == 'B']['pct_of_product_total'].sum()
    check.is_true(abs(product_a_sum - 1.0) < 0.01, "P20: Product A percentages sum to 1", "Product A percentages should sum to 1.0")
    check.is_true(abs(product_b_sum - 1.0) < 0.01, "P20: Product B percentages sum to 1", "Product B percentages should sum to 1.0")
    check.all_values_in_range(df['pct_of_product_total'], 0, 1, "P20: Values in range")
