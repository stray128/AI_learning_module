from utils.checker import check
import numpy as np
import pandas as pd

def p0(globals_dict):
    check.is_true('np' in globals_dict, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in globals_dict, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('stats' in globals_dict, "P0c: Stats imported", "Import stats from scipy")

def p1(mean_val):
    check.is_not_none(mean_val, "P1: Not None")
    check.is_type(mean_val, (int, float, np.number), "P1: Type check")
    check.value_in_range(mean_val, 25, 35, "P1: Reasonable range")

def p2(median_val):
    check.is_not_none(median_val, "P2: Not None")
    check.is_type(median_val, (int, float, np.number), "P2: Type check")
    check.value_in_range(median_val, 5, 7, "P2: Reasonable range")

def p3(mode_val):
    check.is_not_none(mode_val, "P3: Not None")
    check.is_type(mode_val, (int, float, np.number), "P3: Type check")
    check.value_in_range(mode_val, 2, 4, "P3: Reasonable range")

def p4(var_val):
    check.is_not_none(var_val, "P4: Not None")
    check.is_type(var_val, (int, float, np.number), "P4: Type check")
    check.value_in_range(var_val, 4, 5, "P4: Reasonable range for sample variance")

def p5(range_val):
    check.is_not_none(range_val, "P5: Not None")
    check.is_type(range_val, (int, float, np.number), "P5: Type check")
    check.is_true(range_val >= 0, "P5: Non-negative", "Range should be non-negative")

def p6(std_val):
    check.is_not_none(std_val, "P6: Not None")
    check.is_type(std_val, (int, float, np.number), "P6: Type check")
    check.value_in_range(std_val, 4.5, 5.5, "P6: Reasonable range")

def p7(q1, q2, q3):
    check.is_not_none(q1, "P7a: Q1 not None")
    check.is_not_none(q2, "P7b: Q2 not None")
    check.is_not_none(q3, "P7c: Q3 not None")
    check.is_true(q1 < q2 < q3, "P7d: Quartiles ordered", "Q1 < Q2 < Q3 should hold")
    check.value_in_range(q2, 49, 52, "P7e: Q2 (median) in reasonable range")

def p8(iqr_val):
    check.is_not_none(iqr_val, "P8: Not None")
    check.is_type(iqr_val, (int, float, np.number), "P8: Type check")
    check.is_true(iqr_val > 0, "P8: Positive IQR", "IQR should be positive")
    check.value_in_range(iqr_val, 80, 95, "P8: Reasonable range")

def p9(outliers):
    check.is_not_none(outliers, "P9: Not None")
    check.is_type(outliers, np.ndarray, "P9: Type check")
    check.is_true(len(outliers) > 0, "P9: Has outliers", "Should detect at least one outlier")
    check.is_true(np.all(outliers > 50), "P9: Outliers are extreme", "Outliers should be much larger than typical values")

def p10(z_scores):
    check.is_not_none(z_scores, "P10: Not None")
    check.is_type(z_scores, np.ndarray, "P10: Type check")
    check.has_length(z_scores, 5, "P10: Correct length")
    check.mean_is_close(z_scores, 0.0, "P10: Mean is 0", tolerance=0.01)
    check.is_true(abs(z_scores[2]) < 0.1, "P10: Middle value z-score", "Middle value should have z-score near 0")

def p11(cv):
    check.is_not_none(cv, "P11: Not None")
    check.is_type(cv, (int, float, np.number), "P11: Type check")
    check.value_in_range(cv, 40, 60, "P11: Reasonable percentage range")

def p12(five_num, data):
    check.is_not_none(five_num, "P12: Not None")
    check.is_type(five_num, (list, np.ndarray), "P12: Type check")
    check.has_length(five_num, 5, "P12: Correct length")
    check.is_true(five_num[0] == np.min(data), "P12a: Min correct", "First element should be minimum")
    check.is_true(five_num[4] == np.max(data), "P12b: Max correct", "Last element should be maximum")
    check.is_sorted(five_num, "P12c: Sorted order", ascending=True)

def p13(skew_val):
    check.is_not_none(skew_val, "P13: Not None")
    check.is_type(skew_val, (int, float, np.number), "P13: Type check")
    check.is_true(skew_val > 0, "P13: Positive skew", "Data is right-skewed, skewness should be positive")

def p14(kurt_val):
    check.is_not_none(kurt_val, "P14: Not None")
    check.is_type(kurt_val, (int, float, np.number), "P14: Type check")
    check.value_in_range(kurt_val, -1, 1, "P14: Normal range for normal distribution")

def p15(weighted_mean, grades):
    check.is_not_none(weighted_mean, "P15: Not None")
    check.is_type(weighted_mean, (int, float, np.number), "P15: Type check")
    check.value_in_range(weighted_mean, np.min(grades), np.max(grades), "P15: Within grade range")
    check.value_in_range(weighted_mean, 85, 90, "P15: Reasonable range")

def p16(desc_stats):
    check.is_not_none(desc_stats, "P16: Not None")
    check.is_type(desc_stats, pd.DataFrame, "P16: Type check")
    check.contains(list(desc_stats.index), 'mean', "P16a: Has mean")
    check.contains(list(desc_stats.columns), 'A', "P16b: Has column A")
    check.contains(list(desc_stats.columns), 'B', "P16c: Has column B")

def p17(corr_val):
    check.is_not_none(corr_val, "P17: Not None")
    check.is_type(corr_val, (int, float, np.number), "P17: Type check")
    check.value_in_range(corr_val, -1, 1, "P17a: Valid correlation range")
    check.is_true(corr_val > 0, "P17b: Positive correlation", "x and y should have positive correlation")
