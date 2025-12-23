from utils.checker import check
import numpy as np
import pandas as pd

def p0(globals_dict):
    check.is_true('np' in globals_dict, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in globals_dict, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('StandardScaler' in globals_dict, "P0c: StandardScaler imported", "Import StandardScaler from sklearn.preprocessing")
    check.is_true('SimpleImputer' in globals_dict, "P0d: SimpleImputer imported", "Import SimpleImputer from sklearn.impute")

def p1(X_scaled):
    check.is_not_none(X_scaled, "P1: Not None")
    check.is_type(X_scaled, np.ndarray, "P1: Type check")
    check.has_shape(X_scaled, (5, 1), "P1: Correct shape")
    check.mean_is_close(X_scaled, 0.0, "P1a: Mean is 0", tolerance=0.01)
    check.std_is_close(X_scaled, 1.0, "P1b: Std is 1", tolerance=0.01)

def p2(X_minmax):
    check.is_not_none(X_minmax, "P2: Not None")
    check.is_type(X_minmax, np.ndarray, "P2: Type check")
    check.has_shape(X_minmax, (5, 1), "P2: Correct shape")
    check.min_value_is(X_minmax, 0.0, "P2a: Min is 0")
    check.max_value_is(X_minmax, 1.0, "P2b: Max is 1")

def p3(X_custom):
    check.is_not_none(X_custom, "P3: Not None")
    check.is_type(X_custom, np.ndarray, "P3: Type check")
    check.min_value_is(X_custom, -1.0, "P3a: Min is -1")
    check.max_value_is(X_custom, 1.0, "P3b: Max is 1")

def p4(mean_, std_):
    check.is_not_none(mean_, "P4a: Mean not None")
    check.is_not_none(std_, "P4b: Std not None")
    check.is_type(mean_, np.ndarray, "P4c: Mean type check")
    check.is_type(std_, np.ndarray, "P4d: Std type check")
    check.is_true(abs(mean_[0] - 30.0) < 0.01, "P4e: Correct mean", "Mean should be 30")
    check.value_in_range(std_[0], 14, 15, "P4f: Reasonable std")

def p5(X_imputed):
    check.is_not_none(X_imputed, "P5: Not None")
    check.is_type(X_imputed, np.ndarray, "P5: Type check")
    check.has_shape(X_imputed, (5, 1), "P5: Correct shape")
    check.is_true(not np.any(np.isnan(X_imputed)), "P5a: No NaN values", "Should have no missing values")
    check.is_true(abs(X_imputed[2, 0] - 3.0) < 0.01, "P5b: Correct imputation", "Missing value should be replaced with mean")

def p6(X_imputed):
    check.is_not_none(X_imputed, "P6: Not None")
    check.is_type(X_imputed, np.ndarray, "P6: Type check")
    check.is_true(not np.any(np.isnan(X_imputed)), "P6a: No NaN values", "Should have no missing values")
    check.is_true(abs(X_imputed[2, 0] - 3.0) < 0.01, "P6b: Correct median imputation", "Should use median")

def p7(X_robust):
    check.is_not_none(X_robust, "P7: Not None")
    check.is_type(X_robust, np.ndarray, "P7: Type check")
    check.has_shape(X_robust, (6, 1), "P7: Correct shape")

def p8(X_scaled):
    check.is_not_none(X_scaled, "P8: Not None")
    check.is_type(X_scaled, np.ndarray, "P8: Type check")
    check.has_shape(X_scaled, (5, 3), "P8: Correct shape")
    check.mean_is_close(X_scaled.mean(axis=0), 0.0, "P8: Column means are 0", tolerance=0.01)

def p9(X_normalized):
    check.is_not_none(X_normalized, "P9: Not None")
    check.is_type(X_normalized, np.ndarray, "P9: Type check")
    check.has_shape(X_normalized, (3, 2), "P9: Correct shape")
    _row_norms = np.linalg.norm(X_normalized, axis=1)
    check.is_true(np.allclose(_row_norms, 1.0), "P9: Unit norm", "Each row should have L2 norm of 1")

def p10(X_imputed):
    check.is_not_none(X_imputed, "P10: Not None")
    check.is_type(X_imputed, np.ndarray, "P10: Type check")
    check.is_true(not np.any(np.isnan(X_imputed)), "P10a: No NaN values", "Should have no missing values")
    check.is_true(X_imputed[2, 0] == 0.0, "P10b: First imputation", "Should be filled with 0")
    check.is_true(X_imputed[4, 0] == 0.0, "P10c: Second imputation", "Should be filled with 0")

def p11(X_train_scaled, X_test_scaled):
    check.is_not_none(X_train_scaled, "P11a: Train not None")
    check.is_not_none(X_test_scaled, "P11b: Test not None")
    check.is_type(X_train_scaled, np.ndarray, "P11c: Train type check")
    check.is_type(X_test_scaled, np.ndarray, "P11d: Test type check")
    check.has_shape(X_train_scaled, (5, 1), "P11e: Train shape")
    check.has_shape(X_test_scaled, (3, 1), "P11f: Test shape")

def p12(X_l1):
    check.is_not_none(X_l1, "P12: Not None")
    check.is_type(X_l1, np.ndarray, "P12: Type check")
    check.has_shape(X_l1, (2, 3), "P12: Correct shape")
    _row_sums = np.abs(X_l1).sum(axis=1)
    check.is_true(np.allclose(_row_sums, 1.0), "P12: L1 norm", "Each row should sum to 1 in absolute value")

def p13(X_original, X):
    check.is_not_none(X_original, "P13: Not None")
    check.is_type(X_original, np.ndarray, "P13: Type check")
    check.has_shape(X_original, (5, 1), "P13: Correct shape")
    check.is_true(np.allclose(X_original, X), "P13: Recovered original", "Should match original values")

def p14(df_imputed):
    check.is_not_none(df_imputed, "P14: Not None")
    check.is_type(df_imputed, pd.DataFrame, "P14: Type check")
    check.has_shape(df_imputed, (5, 3), "P14: Correct shape")
    check.has_no_nulls(df_imputed, "P14: No missing values")

def p15(X_standard, X_minmax, X_robust):
    check.is_not_none(X_standard, "P15a: Standard not None")
    check.is_not_none(X_minmax, "P15b: MinMax not None")
    check.is_not_none(X_robust, "P15c: Robust not None")
    check.has_shape(X_standard, (6, 1), "P15d: Standard shape")
    check.has_shape(X_minmax, (6, 1), "P15e: MinMax shape")
    check.has_shape(X_robust, (6, 1), "P15f: Robust shape")

def p16(X_maxabs):
    check.is_not_none(X_maxabs, "P16: Not None")
    check.is_type(X_maxabs, np.ndarray, "P16: Type check")
    check.has_shape(X_maxabs, (5, 1), "P16: Correct shape")
    check.is_true(abs(np.abs(X_maxabs).max() - 1.0) < 0.01, "P16: Max abs is 1", "Maximum absolute value should be 1")
    check.all_values_in_range(X_maxabs, -1, 1, "P16: In range [-1, 1]")

def p17(X_power):
    check.is_not_none(X_power, "P17: Not None")
    check.is_type(X_power, np.ndarray, "P17: Type check")
    check.has_shape(X_power, (7, 1), "P17: Correct shape")
