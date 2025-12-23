from utils.checker import check
import numpy as np

def p1(max_val):
    check.is_not_none(max_val, "P1: Value check")
    check.is_true(max_val == 9, "P1: Maximum value", "Should be 9")

def p2(max_idx):
    check.is_not_none(max_idx, "P2: Value check")
    check.is_true(max_idx == 5, "P2: Index of maximum", "Should be 5")

def p3(std_val):
    check.is_not_none(std_val, "P3: Value check")
    check.is_true(np.isclose(std_val, 2.0), "P3: Standard deviation", "Should be approximately 2.0")

def p4(sorted_arr):
    check.is_type(sorted_arr, np.ndarray, "P4: Type check")
    check.has_length(sorted_arr, 8, "P4: Length check")
    check.first_element_is(sorted_arr, 1, "P4: First element")
    check.last_element_is(sorted_arr, 9, "P4: Last element")
    check.is_sorted(sorted_arr, "P4: Should be sorted")

def p5(unique):
    check.is_type(unique, np.ndarray, "P5: Type check")
    check.has_length(unique, 4, "P5: Length check")
    check.first_element_is(unique, 1, "P5: First element")
    check.last_element_is(unique, 4, "P5: Last element")
    check.is_sorted(unique, "P5: Should be sorted")

def p6(median_val):
    check.is_not_none(median_val, "P6: Value check")
    check.is_true(np.isclose(median_val, 5.0), "P6: Median value", "Should be 5.0")

def p7(p75):
    check.is_not_none(p75, "P7: Value check")
    check.is_true(np.isclose(p75, 75.75), "P7: 75th percentile", "Should be approximately 75.75")

def p8(random_ints):
    check.is_type(random_ints, np.ndarray, "P8: Type check")
    check.has_length(random_ints, 10, "P8: Length check")
    check.all_values_in_range(random_ints, 1, 100, "P8: Range check")
    check.is_true(random_ints.dtype in [np.int32, np.int64], "P8: Integer type", "Should be integer type")

def p9(normal_samples):
    check.is_type(normal_samples, np.ndarray, "P9: Type check")
    check.has_length(normal_samples, 1000, "P9: Length check")
    check.mean_is_close(normal_samples, 50, "P9: Mean check", tolerance=2)
    check.std_is_close(normal_samples, 10, "P9: Std check", tolerance=1)

def p10(sort_indices):
    check.is_type(sort_indices, np.ndarray, "P10: Type check")
    check.has_length(sort_indices, 4, "P10: Length check")
    check.first_element_is(sort_indices, 1, "P10: First element")
    check.last_element_is(sort_indices, 2, "P10: Last element")
    # Verify it actually sorts the array
    arr = np.array([30, 10, 40, 20])
    check.is_sorted(arr[sort_indices], "P10: Should produce sorted array")

def p11(transposed):
    check.is_type(transposed, np.ndarray, "P11: Type check")
    check.has_shape(transposed, (4, 3), "P11: Shape check")
    check.first_element_is(transposed.flatten(), 0, "P11: First element")
    matrix = np.arange(12).reshape(3, 4)
    check.is_true(transposed[1, 2] == matrix[2, 1], "P11: Transpose property", "T[i,j] should equal original[j,i]")

def p12(A_inv):
    check.is_type(A_inv, np.ndarray, "P12: Type check")
    check.has_shape(A_inv, (2, 2), "P12: Shape check")
    # Verify A @ A_inv ≈ I
    A = np.array([[1, 2], [3, 4]])
    identity = A @ A_inv
    check.is_true(np.allclose(identity, np.eye(2)), "P12: Inverse property", "A @ A_inv should equal identity matrix")

def p13(corr):
    check.is_not_none(corr, "P13: Value check")
    check.is_true(np.isclose(corr, 1.0), "P13: Correlation value", "Should be 1.0")

def p14(cov_matrix):
    check.is_type(cov_matrix, np.ndarray, "P14: Type check")
    check.has_shape(cov_matrix, (2, 2), "P14: Shape check")
    check.is_true(np.isclose(cov_matrix[0, 1], -2.5), "P14: Covariance value", "Should be -2.5")

def p15(eigenvalues):
    check.is_type(eigenvalues, np.ndarray, "P15: Type check")
    check.has_length(eigenvalues, 2, "P15: Length check")
    check.is_true(np.isclose(np.sum(eigenvalues), 7), "P15: Sum of eigenvalues", "Should equal trace (7)")
