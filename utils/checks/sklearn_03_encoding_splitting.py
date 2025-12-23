from utils.checker import check
import numpy as np
import pandas as pd

def p0(globals_dict):
    check.is_true('np' in globals_dict, "P0a: NumPy imported", "Import numpy as np")
    check.is_true('pd' in globals_dict, "P0b: Pandas imported", "Import pandas as pd")
    check.is_true('LabelEncoder' in globals_dict, "P0c: LabelEncoder imported", "Import LabelEncoder from sklearn.preprocessing")
    check.is_true('OneHotEncoder' in globals_dict, "P0d: OneHotEncoder imported", "Import OneHotEncoder from sklearn.preprocessing")
    check.is_true('train_test_split' in globals_dict, "P0e: train_test_split imported", "Import train_test_split from sklearn.model_selection")

def p1(y_encoded):
    check.is_not_none(y_encoded, "P1: Not None")
    check.is_type(y_encoded, np.ndarray, "P1: Type check")
    check.has_length(y_encoded, 5, "P1: Correct length")
    check.is_true(len(np.unique(y_encoded)) == 3, "P1: Three unique values", "Should have 3 unique encoded values")

def p2(classes):
    check.is_not_none(classes, "P2: Not None")
    check.is_type(classes, np.ndarray, "P2: Type check")
    check.has_length(classes, 3, "P2: Correct length")
    check.contains(list(classes), 'apple', "P2a: Contains apple")
    check.contains(list(classes), 'banana', "P2b: Contains banana")
    check.contains(list(classes), 'cherry', "P2c: Contains cherry")

def p3(X_train, X_test):
    check.is_not_none(X_train, "P3a: X_train not None")
    check.is_not_none(X_test, "P3b: X_test not None")
    check.has_length(X_train, 40, "P3c: Train size")
    check.has_length(X_test, 10, "P3d: Test size")

def p4(X_train, X_test):
    check.is_not_none(X_train, "P4a: X_train not None")
    check.is_not_none(X_test, "P4b: X_test not None")
    check.has_length(X_train, 8, "P4c: Train size")
    check.has_length(X_test, 2, "P4d: Test size")

def p5(X_encoded):
    check.is_not_none(X_encoded, "P5: Not None")
    check.is_type(X_encoded, np.ndarray, "P5: Type check")
    check.has_shape(X_encoded, (4, 3), "P5a: Correct shape")
    _row_sums = X_encoded.sum(axis=1)
    check.is_true(np.allclose(_row_sums, 1.0), "P5b: Row sums", "Each row should sum to 1")

def p6(y_decoded, categories):
    check.is_not_none(y_decoded, "P6: Not None")
    check.is_type(y_decoded, np.ndarray, "P6: Type check")
    check.has_length(y_decoded, 5, "P6: Correct length")
    check.is_true(list(y_decoded) == categories, "P6: Matches original", "Should match original categories")

def p7(categories):
    check.is_not_none(categories, "P7: Not None")
    check.is_type(categories, list, "P7: Type check")
    check.has_length(categories, 1, "P7a: One feature")
    check.has_length(categories[0], 3, "P7b: Three categories")
    check.contains(list(categories[0]), 'small', "P7c: Contains small")

def p8(X_train, y_test):
    check.is_not_none(X_train, "P8a: X_train not None")
    check.is_not_none(y_test, "P8b: y_test not None")
    check.has_length(X_train, 40, "P8c: Train size")
    check.has_length(y_test, 10, "P8d: Test size")
    _test_ratio = y_test.sum() / len(y_test)
    check.value_in_range(_test_ratio, 0.15, 0.25, "P8e: Maintains class distribution")

def p9(X_encoded):
    check.is_not_none(X_encoded, "P9: Not None")
    check.is_type(X_encoded, np.ndarray, "P9: Type check")
    check.has_shape(X_encoded, (5, 1), "P9: Correct shape")
    check.is_true(X_encoded[0, 0] == 0.0, "P9a: low = 0", "'low' should be encoded as 0")
    check.is_true(X_encoded[2, 0] == 2.0, "P9b: high = 2", "'high' should be encoded as 2")

def p10(X_encoded):
    check.is_not_none(X_encoded, "P10: Not None")
    check.is_type(X_encoded, np.ndarray, "P10: Type check")
    check.has_shape(X_encoded, (4, 2), "P10: Correct shape (k-1 columns)")

def p11(X_train, y_test):
    check.is_not_none(X_train, "P11a: X_train not None")
    check.is_not_none(y_test, "P11b: y_test not None")
    check.has_length(X_train, 4, "P11c: Train size")
    check.has_length(y_test, 1, "P11d: Test size")
    check.is_true(y_test[-1] == 4, "P11e: Last element", "Without shuffle, last test element should be 4")

def p12(X_encoded):
    check.is_not_none(X_encoded, "P12: Not None")
    check.is_type(X_encoded, np.ndarray, "P12: Type check")
    check.has_shape(X_encoded, (4, 6), "P12: Correct shape (3+3 columns)")

def p13(X_test_encoded):
    check.is_not_none(X_test_encoded, "P13: Not None")
    check.is_type(X_test_encoded, np.ndarray, "P13: Type check")
    check.has_shape(X_test_encoded, (2, 3), "P13: Correct shape")
    check.is_true(np.array_equal(X_test_encoded[1], np.zeros(3)), "P13: Unknown as zeros", "Unknown category should be all zeros")

def p14(X_train_enc, X_test_enc):
    check.is_not_none(X_train_enc, "P14a: Train not None")
    check.is_not_none(X_test_enc, "P14b: Test not None")
    check.has_shape(X_train_enc, (8, 3), "P14c: Train shape")
    check.has_shape(X_test_enc, (2, 3), "P14d: Test shape")

def p15(feature_names):
    check.is_not_none(feature_names, "P15: Not None")
    check.is_type(feature_names, np.ndarray, "P15: Type check")
    check.has_length(feature_names, 3, "P15: Correct length")

def p16(n_folds):
    check.is_not_none(n_folds, "P16: Not None")
    check.is_type(n_folds, int, "P16: Type check")
    check.is_true(n_folds == 5, "P16: Correct count", "Should have 5 folds")
