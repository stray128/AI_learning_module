from utils.checker import check
import numpy as np

def p1(result):
    check.is_type(result, np.ndarray, "P1: Type check")
    check.has_length(result, 3, "P1: Length check")
    check.first_element_is(result, 5, "P1: First element")
    check.last_element_is(result, 9, "P1: Last element")
    check.sum_is(result, 21, "P1: Sum check")

def p2(scaled):
    check.is_type(scaled, np.ndarray, "P2: Type check")
    check.has_length(scaled, 5, "P2: Length check")
    check.first_element_is(scaled, 3, "P2: First element")
    check.last_element_is(scaled, 15, "P2: Last element")
    check.sum_is(scaled, 45, "P2: Sum check")

def p3(squared):
    check.is_type(squared, np.ndarray, "P3: Type check")
    check.has_length(squared, 5, "P3: Length check")
    check.first_element_is(squared, 1, "P3: First element")
    check.last_element_is(squared, 25, "P3: Last element")
    check.sum_is(squared, 55, "P3: Sum check")

def p4(roots):
    check.is_type(roots, np.ndarray, "P4: Type check")
    check.has_length(roots, 5, "P4: Length check")
    check.first_element_is(roots, 1.0, "P4: First element")
    check.last_element_is(roots, 5.0, "P4: Last element")
    check.sum_is(roots, 15.0, "P4: Sum check")

def p5(total):
    check.is_not_none(total, "P5: Value check")
    check.is_true(total == 15, "P5: Sum value", "Should be the sum of 1+2+3+4+5")

def p6(result):
    check.is_type(result, np.ndarray, "P6: Type check")
    check.has_shape(result, (3, 3), "P6: Shape check")
    check.first_element_is(result.flatten(), 2, "P6: First element")
    check.last_element_is(result.flatten(), 4, "P6: Last element")
    check.is_true(np.all(result[0] == result[1]), "P6: Rows identical", "All rows should be the same")

def p7(mean_val):
    check.is_not_none(mean_val, "P7: Value check")
    check.is_true(np.isclose(mean_val, 30.0), "P7: Mean value", "Should be 30.0")

def p8(col_sums):
    check.is_type(col_sums, np.ndarray, "P8: Type check")
    check.has_length(col_sums, 4, "P8: Length check")
    check.first_element_is(col_sums, 12, "P8: First element")
    check.last_element_is(col_sums, 21, "P8: Last element")

def p9(row_means):
    check.is_type(row_means, np.ndarray, "P9: Type check")
    check.has_length(row_means, 3, "P9: Length check")
    check.first_element_is(row_means, 1.5, "P9: First element")
    check.last_element_is(row_means, 9.5, "P9: Last element")

def p10(dot):
    check.is_not_none(dot, "P10: Value check")
    check.is_true(dot == 32, "P10: Dot product value", "Should be 32")

def p11(product):
    check.is_type(product, np.ndarray, "P11: Type check")
    check.has_shape(product, (2, 2), "P11: Shape check")
    check.first_element_is(product.flatten(), 22, "P11: First element")
    check.element_at_is(product, (1, 1), 64, "P11: Element at [1,1]")

def p12(normalized):
    check.is_type(normalized, np.ndarray, "P12: Type check")
    check.has_length(normalized, 5, "P12: Length check")
    check.min_value_is(normalized, 0.0, "P12: Minimum value")
    check.max_value_is(normalized, 1.0, "P12: Maximum value")
    check.element_at_is(normalized, 2, 0.5, "P12: Middle element")

def p13(outer):
    check.is_type(outer, np.ndarray, "P13: Type check")
    check.has_shape(outer, (3, 2), "P13: Shape check")
    check.first_element_is(outer.flatten(), 4, "P13: First element")
    check.last_element_is(outer.flatten(), 15, "P13: Last element")
    check.sum_is(outer, 45, "P13: Sum check")

def p14(cumsum):
    check.is_type(cumsum, np.ndarray, "P14: Type check")
    check.has_length(cumsum, 5, "P14: Length check")
    check.first_element_is(cumsum, 1, "P14: First element")
    check.last_element_is(cumsum, 15, "P14: Last element")
    check.is_sorted(cumsum, "P14: Should be sorted")

def p15(norm):
    check.is_not_none(norm, "P15: Value check")
    check.is_true(np.isclose(norm, 5.0), "P15: Norm value", "Should be 5.0")
